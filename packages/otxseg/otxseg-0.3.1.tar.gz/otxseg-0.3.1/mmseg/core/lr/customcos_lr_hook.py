# Copyright (C) 2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
#

import math

from mmcv.runner.hooks import HOOKS

from .base_lr_hook import BaseLrUpdaterHook


@HOOKS.register_module()
class CustomcosLrUpdaterHook(BaseLrUpdaterHook):
    def __init__(self, periods, restart_weights=None, min_lr_ratio=1e-3,
                 top_lr_fractions=None, alpha=1.0, **kwargs):
        super(CustomcosLrUpdaterHook, self).__init__(**kwargs)

        assert isinstance(periods, (tuple, list))
        assert len(periods) > 0

        if restart_weights is None:
            restart_weights = [1.0] * len(periods)
        assert len(periods) == len(restart_weights)

        if top_lr_fractions is None:
            top_lr_fractions = [0.0] * len(periods)
        elif isinstance(top_lr_fractions, (int, float)):
            top_lr_fractions = [top_lr_fractions] * len(periods)
        assert len(periods) == len(top_lr_fractions)

        self.iter_periods = periods
        self.restart_weights = restart_weights
        self.min_lr_ratio = min_lr_ratio
        self.top_lr_fractions = top_lr_fractions
        self.alpha = alpha

        self.iter_cumulative_periods = None
        self.max_iters = None

    def _init_states(self, runner):
        super(CustomcosLrUpdaterHook, self)._init_states(runner)

        if self.by_epoch:
            self.iter_periods = [
                period * self.epoch_len for period in self.iter_periods
            ]

        self.iter_cumulative_periods = [
            sum(self.iter_periods[0:(i + 1)]) for i in range(len(self.iter_periods))
        ]
        self.max_iters = self.iter_cumulative_periods[-1]

    def get_lr(self, runner, base_lr):
        progress = runner.iter
        skip_iters = self.fixed_iters + self.warmup_iters
        if progress <= skip_iters:
            return base_lr
        elif progress > skip_iters + self.max_iters:
            return base_lr * self.min_lr_ratio

        progress -= skip_iters

        idx = self._get_position_from_periods(progress, self.iter_cumulative_periods)
        current_weight = self.restart_weights[idx]
        current_top_lr_fraction = self.top_lr_fractions[idx]
        nearest_restart = 0 if idx == 0 else self.iter_cumulative_periods[idx - 1]
        current_periods = self.iter_periods[idx]

        alpha = min(float(progress - nearest_restart) / float(current_periods), 1.0)
        target_lr = base_lr * self.min_lr_ratio
        out_lr = self._annealing_cos(
            base_lr, target_lr, alpha, current_weight, current_top_lr_fraction, self.alpha
        )

        return out_lr

    @staticmethod
    def _get_position_from_periods(iteration, cumulative_periods):
        for i, period in enumerate(cumulative_periods):
            if iteration < period:
                return i

        raise ValueError(f'Current iteration {iteration} exceeds '
                         f'cumulative_periods {cumulative_periods}')

    @staticmethod
    def _annealing_cos(start, end, progress, weight=1.0, max_fraction=0.0, alpha=1.0):
        if progress < max_fraction:
            return weight * start

        progress = (progress - max_fraction) / (1.0 - max_fraction)

        scale = 0.5 * (math.cos(math.pi * (progress ** alpha)) + 1.0)
        out_value = end + (weight * start - end) * scale

        return out_value
