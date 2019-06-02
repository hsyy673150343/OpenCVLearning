# -*- coding:utf8 -*-
# @TIME     :2019/6/2 20:57
# @Author   : 洪松
# @File     : test_1.py

import cv2 as cv

'''
imshow()--->两个参数：显示图像的帧名称以及要显示的图像本身
waitKey()
'''
img = cv.imread(r'D:\1.png')
cv.imshow('my_image', img)
cv.waitKey()
'''destroyAllWindows()函数可以释放由OpenCV创建的所有窗口'''
cv.destroyAllWindows()