#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/5/13 10:24
#@Author: yangjian
#@File  : path.py

import sys

import os

# 训练数据的路径
DATA_PATH = os.path.join(sys.path[0], 'data', 'input')
# 模型保存的路径
MODEL_PATH = os.path.join(sys.path[0], 'data', 'output', 'model')
# 训练log的输出路径
LOG_PATH = os.path.join(sys.path[0], 'data', 'output', 'logs')