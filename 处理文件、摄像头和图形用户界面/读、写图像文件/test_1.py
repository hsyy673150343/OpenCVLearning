# -*- coding:utf8 -*-
# @TIME     :2019/6/2 16:01
# @Author   : 洪松
# @File     : test_1.py

import numpy as np
import cv2 as cv
'''每个像素都会有一个值，但不同格式表示像素的方式有所不同'''
img_1 = np.zeros((3, 3), dtype=np.uint8)
'''每个像素都由一个8位整数来表示,即每个像素值的范围是0-255'''
'''利用cv.cvtColor函数将该图像转换成BGR格式'''
img_2 = cv.cvtColor(img_1, cv.COLOR_GRAY2BGR)
print('img_1:\n{}'.format(img_1))
print('img_2:\n{}'.format(img_2))
print('shape 0f img_2:\n{}'.format(img_2.shape))
'''
shape 0f img_2:
(3, 3, 3)
表明每个像素存在三个通道
'''

