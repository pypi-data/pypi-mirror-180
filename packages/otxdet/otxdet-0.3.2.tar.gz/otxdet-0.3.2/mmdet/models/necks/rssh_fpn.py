# Copyright (C) 2020-2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions
# and limitations under the License.

import torch
import torch.nn as nn
from mmcv.runner import auto_fp16

from .fpn import FPN
from ..builder import NECKS
from mmcv.cnn import ConvModule


class RSSH(nn.Module):
    def __init__(self, in_channels, conv_cfg, norm_cfg, act_cfg):
        super(RSSH, self).__init__()
        self.in_channels = in_channels
        self.act_cfg = act_cfg

        self.conv1 = ConvModule(
            in_channels,
            in_channels // 2,
            1,
            conv_cfg=conv_cfg,
            norm_cfg=norm_cfg,
            act_cfg=self.act_cfg,
            inplace=False)

        self.conv2 = ConvModule(
            in_channels // 2,
            in_channels // 4,
            1,
            conv_cfg=conv_cfg,
            norm_cfg=norm_cfg,
            act_cfg=self.act_cfg,
            inplace=False)

        self.conv3 = ConvModule(
            in_channels // 4,
            in_channels // 4,
            1,
            conv_cfg=conv_cfg,
            norm_cfg=norm_cfg,
            act_cfg=self.act_cfg,
            inplace=False)

    def forward(self, inputs):
        x1 = self.conv1(inputs)
        x2 = self.conv2(x1)
        x3 = self.conv3(x2)

        return torch.cat((x1, x2, x3), axis=1)


@NECKS.register_module()
class RSSH_FPN(FPN):

    def __init__(self,
                 in_channels,
                 out_channels,
                 num_outs,
                 start_level=0,
                 end_level=-1,
                 add_extra_convs=False,
                 extra_convs_on_inputs=True,
                 relu_before_extra_convs=False,
                 no_norm_on_lateral=False,
                 conv_cfg=None,
                 norm_cfg=None,
                 act_cfg=None):
        super().__init__(in_channels,
                         out_channels,
                         num_outs,
                         start_level,
                         end_level,
                         add_extra_convs,
                         extra_convs_on_inputs,
                         relu_before_extra_convs,
                         no_norm_on_lateral,
                         conv_cfg,
                         norm_cfg,
                         act_cfg)

        self.context_modules = \
            nn.ModuleList(
                [RSSH(out_channels, conv_cfg, norm_cfg, act_cfg) for _ in self.fpn_convs])

    @auto_fp16()
    def forward(self, inputs):
        outs = super().forward(inputs)
        outs = [self.context_modules[i](out) for i, out in enumerate(outs)]
        return tuple(outs)
