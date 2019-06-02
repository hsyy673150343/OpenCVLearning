# -*- coding:utf8 -*-
# @TIME     :2019/6/2 18:09
# @Author   : 洪松
# @File     : test_5.py

import cv2 as cv

img = cv.imread('2.jpg')
'''shape 返回包括宽度、高度和通道数(如果图像时彩色的),如果图像是单色或灰度的,将不包含通道值'''
print(img.shape)
'''size 该属性是指图像的像素大小'''
print(img.size)
'''dtype 该属性会得到图像的数据类型'''
print(img.dtype)