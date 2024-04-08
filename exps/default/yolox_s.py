#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.num_classes = 4
        # self.depth = 0.33
        # self.width = 0.50

        self.depth = 1.00
        self.width = 1.00
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]
