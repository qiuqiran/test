#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://developers.google.com/machine-learning/crash-course/ml-intro?hl=zh-cn
# http://www.tensorfly.cn/tfdoc/get_started/introduction.html

import tensorflow as tf
import numpy as np

# 使用 NumPy 生成假数据(phony data), 总共 100 个点.
x_data = np.float32(np.random.rand(2,100))
y_data = np.dot([0.100, 0.200], x_data) + 0.300
print(x_data)