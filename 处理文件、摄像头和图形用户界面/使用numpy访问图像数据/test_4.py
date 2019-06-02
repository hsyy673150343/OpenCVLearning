# -*- coding:utf8 -*-
# @TIME     :2019/6/2 18:05
# @Author   : 洪松
# @File     : test_4.py

import cv2 as cv

img = cv.imread('2.jpg')
my_roi = img[0:100, 0:100]
img[300:400, 300:400] = my_roi
cv.imwrite('2_result.jpg', img)