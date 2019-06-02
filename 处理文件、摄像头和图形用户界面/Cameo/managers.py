# -*- coding:utf8 -*-
# @TIME     :2019/6/2 21:30
# @Author   : 洪松
# @File     : managers.py

import cv2 as cv
import numpy as np
import time

class CaptureManager:

    def __init__(self, capture, preview_window_manager=None, should_mirror_preview=False):
        self.preview_window_manager = preview_window_manager
        self.should_mirror_preview = should_mirror_preview
        self._capture = capture

        self._channel = 0
        self._entered_frame = False
        self._frame = None
        self._image_filename = None
        self._video_filename = None
        self._video_encoding = None
        self._video_writer = None

        self._start_time = None
        self._frame_elapsed = None
        self._fps_estimate = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        if self._channel != value:
            self._channel = value
            self._frame = None
    @property
    def frame(self):
        if self._entered_frame and self._frame is None:
            _, self._frame = self._capture.retrieve()
        return self._frame

    @property
    def is_writing_image(self):
        return self._image_filename is not None

    @property
    def is_writing_video(self):
        return self._video_filename is not None
