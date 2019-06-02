# -*- coding:utf8 -*-
# @TIME     :2019/6/2 17:20
# @Author   : 洪松
# @File     : test_1.py

import cv2 as cv
import numpy as np
import os

'''将含有随机字节的bytearray转换为灰度图像和BGR图像'''

'''os.urandom()函数可随机生成原始字节'''
random_byte_array = bytearray(os.urandom(120000))
flat_numpy_array = np.array(random_byte_array)

gray_image = flat_numpy_array.reshape(300, 400)
cv.imwrite('random_gray.png', gray_image)

bgr_image = flat_numpy_array.reshape(100, 400, 3)
cv.imwrite('random_color.png', bgr_image)