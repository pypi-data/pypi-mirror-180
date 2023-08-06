# Copyright (C) 2018-2021 OpenMMLab
# SPDX-License-Identifier: Apache-2.0
#
# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
#
from .base_roi_head import BaseRoIHead
from .bbox_heads import (BBoxHead, ConvFCBBoxHead, DoubleConvFCBBoxHead,
                         SCNetBBoxHead, Shared2FCBBoxHead,
                         Shared4Conv1FCBBoxHead)
from .cascade_roi_head import CascadeRoIHead
from .double_roi_head import DoubleHeadRoIHead
from .dynamic_roi_head import DynamicRoIHead
from .grid_roi_head import GridRoIHead
from .htc_roi_head import HybridTaskCascadeRoIHead
from .mask_heads import (CoarseMaskHead, FCNMaskHead, FeatureRelayHead,
                         FusedSemanticHead, GlobalContextHead, GridHead,
                         HTCMaskHead, MaskIoUHead, MaskPointHead,
                         SCNetMaskHead, SCNetSemanticHead)
from .mask_scoring_roi_head import MaskScoringRoIHead
from .pisa_roi_head import PISARoIHead
from .point_rend_roi_head import PointRendRoIHead
from .roi_extractors import SingleRoIExtractor
from .scnet_roi_head import SCNetRoIHead
from .shared_heads import ResLayer
from .standard_roi_head_with_text import StandardRoIHeadWithText
from .text_heads import TextRecognitionHeadAttention
from .sparse_roi_head import SparseRoIHead
from .standard_roi_head import StandardRoIHead
from .trident_roi_head import TridentRoIHead

__all__ = [
    'BaseRoIHead', 'CascadeRoIHead', 'DoubleHeadRoIHead', 'MaskScoringRoIHead',
    'HybridTaskCascadeRoIHead', 'GridRoIHead', 'ResLayer', 'BBoxHead',
    'ConvFCBBoxHead', 'Shared2FCBBoxHead', 'StandardRoIHead',
    'Shared4Conv1FCBBoxHead', 'DoubleConvFCBBoxHead', 'FCNMaskHead',
    'HTCMaskHead', 'FusedSemanticHead', 'GridHead', 'MaskIoUHead',
    'SingleRoIExtractor', 'PISARoIHead', 'PointRendRoIHead', 'MaskPointHead',
    'CoarseMaskHead', 'DynamicRoIHead', 'SparseRoIHead', 'TridentRoIHead',
    'SCNetRoIHead', 'SCNetMaskHead', 'SCNetSemanticHead', 'SCNetBBoxHead',
    'FeatureRelayHead', 'GlobalContextHead', 'StandardRoIHeadWithText',
    'TextRecognitionHeadAttention'
]
