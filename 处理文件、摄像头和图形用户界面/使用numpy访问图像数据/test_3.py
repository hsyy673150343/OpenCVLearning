# -*- coding:utf8 -*-
# @TIME     :2019/6/2 17:55
# @Author   : 洪松
# @File     : test_3.py
import cv2 as cv

'''操作通道：将指定通道(B,G和R)的所有值设置为零'''
img = cv.imread('1.jpg')
'''像素操作是一个高代价的低效操作,特别是在视频数据处理时，会发现要等很久才能得到结果'''
'''将图像所有的G(绿色)值设为0'''
img[:,:, 1] = 0
cv.imwrite('1_result.jpg', img)