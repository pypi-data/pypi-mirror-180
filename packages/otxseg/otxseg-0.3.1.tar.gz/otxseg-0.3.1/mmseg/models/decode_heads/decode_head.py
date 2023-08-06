# Copyright (c) 2020-2021 The MMSegmentation Authors
# SPDX-License-Identifier: Apache-2.0
#
# Copyright (C) 2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
#

from abc import ABCMeta, abstractmethod

import torch
import torch.nn as nn
import torch.nn.functional as F
from mmcv.cnn import normal_init
from mmcv.runner import auto_fp16, force_fp32

from mmseg.core import normalize, add_prefix, AngularPWConv
from mmseg.models.utils import IterativeAggregator, IterativeConcatAggregator
from mmseg.ops import resize
from ..builder import build_loss
from ..losses import accuracy, LossEqualizer


class BaseDecodeHead(nn.Module, metaclass=ABCMeta):
    """Base class for BaseDecodeHead.

    Args:
        in_channels (int|Sequence[int]): Input channels.
        channels (int): Channels after modules, before conv_seg.
        num_classes (int): Number of classes.
        dropout_ratio (float): Ratio of dropout layer. Default: 0.1.
        conv_cfg (dict|None): Config of conv layers. Default: None.
        norm_cfg (dict|None): Config of norm layers. Default: None.
        act_cfg (dict): Config of activation layers.
            Default: dict(type='ReLU')
        in_index (int|Sequence[int]): Input feature index. Default: -1
        input_transform (str|None): Transformation type of input features.
            Options: 'resize_concat', 'multiple_select', None.
            'resize_concat': Multiple feature maps will be resize to the
                same size as first one and than concat together.
                Usually used in FCN head of HRNet.
            'multiple_select': Multiple feature maps will be bundle into
                a list and passed into decode head.
            None: Only one select feature map is allowed.
            Default: None.
        loss_decode (dict): Config of decode loss.
            Default: dict(type='CrossEntropyLoss').
        ignore_index (int | None): The label index to be ignored. When using
            masked BCE loss, ignore_index should be set to None. Default: 255
        sampler (dict|None): The config of segmentation map sampler.
            Default: None.
        align_corners (bool): align_corners argument of F.interpolate.
            Default: False.
    """

    def __init__(self,
                 in_channels,
                 channels,
                 *,
                 num_classes,
                 dropout_ratio=0.1,
                 conv_cfg=None,
                 norm_cfg=None,
                 act_cfg=dict(type='ReLU'),
                 in_index=-1,
                 input_transform=None,
                 loss_decode=dict(
                     type='CrossEntropyLoss',
                     use_sigmoid=False,
                     loss_weight=1.0),
                 ignore_index=255,
                 align_corners=False,
                 enable_aggregator=False,
                 aggregator_min_channels=None,
                 aggregator_merge_norm=None,
                 aggregator_use_concat=False,
                 enable_out_seg=True,
                 enable_out_norm=False,
                 enable_loss_equalizer=False,
                 loss_target='gt_semantic_seg',
                 **kwargs):
        super(BaseDecodeHead, self).__init__()

        self._init_inputs(in_channels, in_index, input_transform)

        self.channels = channels
        self.num_classes = num_classes
        self.dropout_ratio = dropout_ratio
        self.conv_cfg = conv_cfg
        self.norm_cfg = norm_cfg
        self.act_cfg = act_cfg
        self.ignore_index = ignore_index
        self.align_corners = align_corners
        self.fp16_enabled = False
        self.enable_out_norm = enable_out_norm
        self.enable_loss_equalizer = enable_loss_equalizer
        self.loss_target = loss_target

        loss_configs = loss_decode if isinstance(loss_decode, (tuple, list)) else [loss_decode]
        assert len(loss_configs) > 0
        self.loss_modules = nn.ModuleList([
            build_loss(loss_cfg, self.ignore_index)
            for loss_cfg in loss_configs
        ])

        self.dropout = None
        if dropout_ratio is not None and dropout_ratio > 0:
            self.dropout = nn.Dropout2d(dropout_ratio)

        self.conv_seg = None
        if enable_out_seg:
            if enable_out_norm:
                self.conv_seg = AngularPWConv(
                    channels,
                    num_classes,
                    clip_output=True
                )
            else:
                self.conv_seg = nn.Conv2d(
                    channels,
                    num_classes,
                    kernel_size=1
                )

        self.aggregator = None
        if enable_aggregator:
            assert isinstance(in_channels, (tuple, list))
            assert len(in_channels) > 1

            self.aggregator = IterativeAggregator(
                in_channels=in_channels,
                min_channels = aggregator_min_channels,
                conv_cfg=self.conv_cfg,
                norm_cfg=self.norm_cfg,
                merge_norm=aggregator_merge_norm,
                use_concat=aggregator_use_concat
            )

            aggregator_min_channels = aggregator_min_channels if aggregator_min_channels is not None else 0
            self.in_channels = max(in_channels[0], aggregator_min_channels)

        self.loss_equalizer = None
        if enable_loss_equalizer:
            self.loss_equalizer = LossEqualizer()
        
        self.forward_output = None

    @property
    def loss_target_name(self):
        return self.loss_target

    @property
    def last_scale(self):
        num_losses = len(self.loss_modules)
        if num_losses <= 0:
            return 1.0

        loss_module = self.loss_modules[0]
        if not hasattr(loss_module, 'last_scale'):
            return 1.0

        return loss_module.last_scale

    def extra_repr(self):
        """Extra repr."""
        s = f'input_transform={self.input_transform}, ' \
            f'ignore_index={self.ignore_index}, ' \
            f'align_corners={self.align_corners}'
        return s

    def _init_inputs(self, in_channels, in_index, input_transform):
        """Check and initialize input transforms.

        The in_channels, in_index and input_transform must match.
        Specifically, when input_transform is None, only single feature map
        will be selected. So in_channels and in_index must be of type int.
        When input_transform

        Args:
            in_channels (int|Sequence[int]): Input channels.
            in_index (int|Sequence[int]): Input feature index.
            input_transform (str|None): Transformation type of input features.
                Options: 'resize_concat', 'multiple_select', None.
                'resize_concat': Multiple feature maps will be resize to the
                    same size as first one and than concat together.
                    Usually used in FCN head of HRNet.
                'multiple_select': Multiple feature maps will be bundle into
                    a list and passed into decode head.
                None: Only one select feature map is allowed.
        """

        if input_transform is not None:
            assert input_transform in ['resize_concat', 'multiple_select']

        self.input_transform = input_transform
        self.in_index = in_index

        if input_transform is not None:
            assert isinstance(in_channels, (list, tuple))
            assert isinstance(in_index, (list, tuple))
            assert len(in_channels) == len(in_index)

            if input_transform == 'resize_concat':
                self.in_channels = sum(in_channels)
            else:
                self.in_channels = in_channels
        else:
            assert isinstance(in_channels, int)
            assert isinstance(in_index, int)

            self.in_channels = in_channels

    def set_step_params(self, init_iter, epoch_size):
        for loss_module in self.loss_modules:
            if hasattr(loss_module, 'set_step_params'):
                loss_module.set_step_params(init_iter, epoch_size)

    def init_weights(self):
        """Initialize weights of classification layer."""

        if self.conv_seg is not None:
            normal_init(self.conv_seg, mean=0, std=0.01)

    def _transform_inputs(self, inputs):
        """Transform inputs for decoder.

        Args:
            inputs (list[Tensor]): List of multi-level img features.

        Returns:
            Tensor: The transformed inputs
        """

        if self.input_transform == 'resize_concat':
            inputs = [inputs[i] for i in self.in_index]
            upsampled_inputs = [
                resize(
                    input=x,
                    size=inputs[0].shape[2:],
                    mode='bilinear',
                    align_corners=self.align_corners) for x in inputs
            ]
            inputs = torch.cat(upsampled_inputs, dim=1)
        elif self.input_transform == 'multiple_select':
            inputs = [inputs[i] for i in self.in_index]
        else:
            inputs = inputs[self.in_index]

        if self.aggregator is not None:
            inputs = self.aggregator(inputs)[0]

        return inputs

    @auto_fp16()
    @abstractmethod
    def forward(self, inputs):
        """Placeholder of forward function."""
        pass

    def forward_train(self, inputs, img_metas, gt_semantic_seg, train_cfg, pixel_weights=None):
        """Forward function for training.
        Args:
            inputs (list[Tensor]): List of multi-level img features.
            img_metas (list[dict]): List of image info dict where each dict
                has: 'img_shape', 'scale_factor', 'flip', and may also contain
                'filename', 'ori_shape', 'pad_shape', and 'img_norm_cfg'.
                For details on the values of these keys see
                `mmseg/datasets/pipelines/formatting.py:Collect`.
            gt_semantic_seg (Tensor): Semantic segmentation masks
                used if the architecture supports semantic segmentation task.
            train_cfg (dict): The training config.
            pixel_weights (Tensor): Pixels weights.

        Returns:
            dict[str, Tensor]: a dictionary of loss components
        """

        seg_logits = self.forward(inputs)
        losses = self.losses(seg_logits, gt_semantic_seg, train_cfg, pixel_weights)

        if self.forward_output is not None:
            return losses, self.forward_output
        else:
            return losses, seg_logits

    def forward_test(self, inputs, img_metas, test_cfg):
        """Forward function for testing.

        Args:
            inputs (list[Tensor]): List of multi-level img features.
            img_metas (list[dict]): List of image info dict where each dict
                has: 'img_shape', 'scale_factor', 'flip', and may also contain
                'filename', 'ori_shape', 'pad_shape', and 'img_norm_cfg'.
                For details on the values of these keys see
                `mmseg/datasets/pipelines/formatting.py:Collect`.
            test_cfg (dict): The testing config.

        Returns:
            Tensor: Output segmentation map.
        """

        seg_logits = self.forward(inputs)
        
        if self.forward_output is not None:
            return self.forward_output
        else:
            return seg_logits

    def cls_seg(self, feat):
        """Classify each pixel."""

        if self.dropout is not None:
            feat = self.dropout(feat)

        if self.enable_out_norm:
            feat = normalize(feat, dim=1, p=2)

        output = self.conv_seg(feat)

        return output

    @staticmethod
    def _mix_loss(logits, target, ignore_index=255):
        num_samples = logits.size(0)
        assert num_samples % 2 == 0

        with torch.no_grad():
            probs = F.softmax(logits, dim=1)
            probs_a, probs_b = torch.split(probs, num_samples // 2)
            mean_probs = 0.5 * (probs_a + probs_b)
            trg_probs = torch.cat([mean_probs, mean_probs], dim=0)

        log_probs = torch.log_softmax(logits, dim=1)
        losses = torch.sum(trg_probs * log_probs, dim=1).neg()

        valid_mask = target != ignore_index
        valid_losses = torch.where(valid_mask, losses, torch.zeros_like(losses))

        return valid_losses.mean()

    @force_fp32(apply_to=('seg_logit', ))
    def losses(self, seg_logit, seg_label, train_cfg, pixel_weights=None):
        """Compute segmentation loss."""

        loss = dict()

        seg_logit = resize(
            input=seg_logit,
            size=seg_label.shape[2:],
            mode='bilinear',
            align_corners=self.align_corners
        )

        seg_label = seg_label.squeeze(1)

        out_losses = dict()
        for loss_idx, loss_module in enumerate(self.loss_modules):
            loss_value, loss_meta = loss_module(
                seg_logit,
                seg_label,
                pixel_weights=pixel_weights
            )

            loss_name = loss_module.name + f'-{loss_idx}'
            out_losses[loss_name] = loss_value
            loss.update(add_prefix(loss_meta, loss_name))

        if self.enable_loss_equalizer and len(self.loss_modules) > 1:
            out_losses = self.loss_equalizer.reweight(out_losses)

        for loss_name, loss_value in out_losses.items():
            loss[loss_name] = loss_value

        loss['loss_seg'] = sum(out_losses.values())
        loss['acc_seg'] = accuracy(seg_logit, seg_label)

        if train_cfg.mix_loss.enable:
            mix_loss = self._mix_loss(
                seg_logit,
                seg_label,
                ignore_index=self.ignore_index
            )

            mix_loss_weight = train_cfg.mix_loss.get('weight', 1.0)
            loss['loss_mix'] = mix_loss_weight * mix_loss

        return loss
