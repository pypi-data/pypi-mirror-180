# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
#
DOMAIN_CUSTOM_OPS_NAME = 'org.openvinotoolkit'

def add_domain(name_operator: str) -> str:
    return DOMAIN_CUSTOM_OPS_NAME + '::' + name_operator
