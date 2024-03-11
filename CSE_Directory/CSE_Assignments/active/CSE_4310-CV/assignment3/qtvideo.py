import sys
import random
import argparse
import numpy as np
np.float = np.float64
np.int = np.int_

from PySide2 import QtCore, QtWidgets, QtGui
from skvideo.io import vread

from KalmanFilter import *
from MotionDetector import *


class QtVideo(QtWidgets.QWidget):
    def __init__(self, frames):
        super().__init__()

        self.frames = frames
        self.starting_frame = 2 # due to initialization of motion detector

        self.motion_detector = MotionDetector(2,10,10,1,100,frames)

        self.current_frame = self.starting_frame

        # Creating Buttons
        self.backward_60 = QtWidgets.QPushButton("-60 Frames")
        self.backward_1 = QtWidgets.QPushButton("-1 Frame")
        self.forward_1 = QtWidgets.QPushButton("+1 Frame")
        self.forward_60 = QtWidgets.QPushButton("+60 Frames")

        # Configure image label
        self.img_label = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.draw_image()

        # Configure slider
        self.frame_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.frame_slider.setTickInterval(1)
        self.frame_slider.setMinimum(self.starting_frame)
        self.frame_slider.setMaximum(self.frames.shape[0]-1)

        # Placing components
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.img_label)
        self.button_layout = QtWidgets.QHBoxLayout(self)
        self.button_layout.addWidget(self.backward_60)
        self.button_layout.addWidget(self.backward_1)
        self.button_layout.addWidget(self.forward_1)
        self.button_layout.addWidget(self.forward_60)
        self.layout.addLayout(self.button_layout)
        self.layout.addWidget(self.frame_slider)

        # Connect functions
        self.backward_60.clicked.connect(lambda: self.on_click(-60))
        self.backward_1.clicked.connect(lambda: self.on_click(-1))
        self.forward_1.clicked.connect(lambda: self.on_click(1))
        self.forward_60.clicked.connect(lambda: self.on_click(60))
        self.frame_slider.sliderMoved.connect(self.on_move)

    @QtCore.Slot()
    def on_click(self, inc):
        # Calculating resulting frame
        desired = self.current_frame + inc
        self.current_frame = max(min(self.frames.shape[0]-1, desired),self.starting_frame)
        self.frame_slider.setValue(desired)

        self.draw_image()

    @QtCore.Slot()
    def on_move(self, pos):
        self.current_frame = pos
        self.draw_image()

    def draw_image(self):
        h, w, c = self.frames[self.current_frame].shape
        if c == 1:
            img = QtGui.QImage(self.frames[self.current_frame], w, h, QtGui.QImage.Format_Grayscale8)
        else:
            img = QtGui.QImage(self.frames[self.current_frame], w, h, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(img)

        # drawing bounding boxes
        painter = QtGui.QPainter(pixmap)
        pen = QtGui.QPen(QtGui.QColor(255,0,0))
        pen.setWidth(2)
        painter.setPen(pen)
        for rect, _ in zip(*self.motion_detector.update(self.current_frame)): # TODO link this to MotionDetector.py
            painter.drawRect(*rect)
        painter.end()

        self.img_label.setPixmap(pixmap)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Demo for loading video with Qt5.")
    parser.add_argument("video_path", metavar='PATH_TO_VIDEO', type=str)
    parser.add_argument("--num_frames", metavar='n', type=int, default=-1)
    parser.add_argument("--grey", metavar='True/False', type=str, default=False)
    args = parser.parse_args()

    num_frames = 60 # args.num_frames

    if num_frames > 0:
        frames = vread(args.video_path, num_frames=num_frames, as_grey=args.grey)
    else:
        frames = vread(args.video_path, as_grey=args.grey)

    app = QtWidgets.QApplication([])

    widget = QtVideo(frames)
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
