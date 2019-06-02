# -*- coding:utf8 -*-
# @TIME     :2019/6/2 17:44
# @Author   : 洪松
# @File     : test_2.py

import cv2 as cv

'''将坐标(150,120)的当前黑色值(2)变为255'''
img = cv.imread('result.png')
'''
item(),三个参数：x,y,以及(x,y)位置的数组索引,该函数能返回索引位置的值
itemset()可设置指定像素在指定通道的值,两个参数：一个三元组(x,y和索引)和要设定的值
'''
print(img.item(150, 120, 0))
img.itemset((150, 120, 0), 255)
print(img.item(150, 120, 0))