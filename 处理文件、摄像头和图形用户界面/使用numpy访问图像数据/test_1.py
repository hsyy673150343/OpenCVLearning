# -*- coding:utf8 -*-
# @TIME     :2019/6/2 17:32
# @Author   : 洪松
# @File     : test_1.py

import cv2 as cv
import numpy as np
'''将BGR图像在(0,0)处的像素转化为白像素'''
'''在BGR图像中,某一位置的数据是按B、G、R这样的顺序保存的三元数组'''
img = cv.imread(r'D:\1.png')
img[0][0] = [255, 255, 255]
cv.imwrite('result.png', img)