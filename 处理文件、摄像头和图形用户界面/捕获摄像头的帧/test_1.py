# -*- coding:utf8 -*-
# @TIME     :2019/6/2 20:40
# @Author   : 洪松
# @File     : test_1.py

import cv2 as cv

'''捕获摄像头10秒的视频信息,并将其写入一个AVI文件中'''

camera_capture = cv.VideoCapture(0)
'''假设的帧速率'''
fps = 30
size = (int(camera_capture.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(camera_capture.get(cv.CAP_PROP_FRAME_HEIGHT)))

video_writer = cv.VideoWriter('E:\my_camera.avi', cv.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size)

success, frame = camera_capture.read()
num_frames_remaining = 10 * fps - 1
while success and num_frames_remaining > 0:
    video_writer.write(frame)
    success, frame = camera_capture.read()
    num_frames_remaining -= 1
camera_capture.release()