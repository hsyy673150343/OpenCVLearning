# -*- coding:utf8 -*-
# @TIME     :2019/6/2 16:57
# @Author   : 洪松
# @File     : test_2.py

import cv2 as cv

gray_image = cv.imread(r"E:\yangyang\3.jpg", cv.IMREAD_GRAYSCALE)
cv.imwrite('result.jpg', gray_image)