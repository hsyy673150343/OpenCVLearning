# -*- coding:utf8 -*-
# @TIME     :2019/6/2 21:03
# @Author   : 洪松
# @File     : test_1.py

import cv2 as cv
'''
OpenCV的namedWindow()、imshow()和DestroyWindow()函数允许指定窗口名来创建、显示和销毁窗口
任何窗口下都可以通过waitKey()函数来获取键盘输入，通过setMouseCallback()函数来获取鼠标输入
'''

'''实时显示摄像头帧'''
clicked = False


def on_mouse(event, x, y, flags, param):
    global clicked
    if event == cv.EVENT_LBUTTONUP:
        clicked = True

'''OpenCV的窗口只有在调用waitKey()函数时才会更新,waitKey()函数只有在OpenCV窗口成为活动窗口时，才能捕获输入信息'''
camera_capture = cv.VideoCapture(0)
cv.namedWindow('MyWindow')
cv.setMouseCallback('MyWindow', on_mouse)
print('Showing camera feed. Click window or press any key to stop.')
success, frame = camera_capture.read()
'''waitKey()的参数为等待键盘触发的时间，单位为毫秒，其返回值是-1(表示没有键被按下)或ASCII码'''
while success and cv.waitKey(1) == -1 and not clicked:
    cv.imshow('MyWindow',frame)
    success, frame = camera_capture.read()

cv.destroyAllWindows('MyWindow')
camera_capture.release()