"""
Interactive Trackbars
=====================
Description: Interactive rectangle positioning using OpenCV trackbars. Adjust position (x, y) and 
size (width, height) of overlay rectangle in real-time using trackbar controls.

Hardware Requirements:
- Raspberry Pi Camera Module

Features: Interactive trackbars, real-time parameter adjustment, rectangle overlay, FPS display

Author: Vilas
"""

from picamera2 import Picamera2
from time import time
import cv2

def TrackX(val):
    global xPos
    xPos = val

def TrackY(val):
    global yPos
    yPos = val

def TrackW(val):
    global boxW
    boxW = val

def TrackH(val):
    global boxH
    boxH = val

cam = Picamera2()
width = 720
height = 360
cam.preview_configuration.main.size = (width, height)
cam.preview_configuration.main.format = 'RGB888'
cam.preview_configuration.align()

cam.configure('preview')
cam.start()

fps = 0
fpspos = (15, 60)
fpscolor = (100, 100, 100)
fpsthickness = 3
fpsheight = 1

cv2.namedWindow('mytrackbar')

cv2.createTrackbar('x pos', 'mytrackbar', 10, width-1, TrackX)
cv2.createTrackbar('y pos', 'mytrackbar', 10, height-1, TrackY)

cv2.createTrackbar('boxW', 'mytrackbar', 10, width-1, TrackW)
cv2.createTrackbar('boxH', 'mytrackbar', 10, height-1, TrackH)

while True:
    sTime = time()
    frame = cam.capture_array()
    cv2.rectangle(frame, (xPos, yPos), (xPos+boxW, yPos+boxH), (0,0,255), 2)
    cv2.putText(frame, str(int(fps)), fpspos, cv2.FONT_HERSHEY_SIMPLEX, fpsheight, fpscolor, fpsthickness)
    cv2.imshow('he', frame)
    if cv2.waitKey(1) == ord('q'):
        break

    fps = 1/(time()-sTime)

cv2.destroyAllWindows()