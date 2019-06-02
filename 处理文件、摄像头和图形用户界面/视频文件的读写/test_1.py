# -*- coding:utf8 -*-
# @TIME     :2019/6/2 18:14
# @Author   : 洪松
# @File     : test_1.py

import cv2 as cv
'''opencv提供了VideoCapture类和VideoWriter类来支持各种格式的视频文件'''

video_capture = cv.VideoCapture('D:\lele.avi')
fps = video_capture.get(cv.CAP_PROP_FPS)
size = (int(video_capture.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(video_capture.get(cv.CAP_PROP_FRAME_HEIGHT)))

video_writer = cv.VideoWriter('E:\lele.avi', cv.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size)

success, frame = video_capture.read()
while success:
    video_writer.write(frame)
    success, frame = video_capture.read()