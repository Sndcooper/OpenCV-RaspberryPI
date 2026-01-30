"""
Bouncing Box Animation
======================
Description: Animated bouncing box overlay on live camera feed. Red rectangle bounces around screen 
edges with physics-based movement. Demonstrates basic animation with video overlay.

Hardware Requirements:
- Raspberry Pi Camera Module

Features: Animation, boundary detection, FPS display

Author: Vilas
"""

import cv2
from time import time
from picamera2 import Picamera2

cam = Picamera2()
width = 640
height = 360
cam.preview_configuration.main.size = (640, 360)
cam.preview_configuration.main.format = ('RGB888')
cam.preview_configuration.align()

cam.configure('preview')
cam.start()

#fps
fps = 0
pos = (15, 60)
height = 1
fcolor = (255, 0, 255)
weight = 3

#bouncing box
boxW = 100 #640
boxH = 60 #360
tl_x = 0
tl_y = 0
br_x = tl_x+boxW
br_y = tl_y+boxH

dx = 5
dy = 5
xtime = 0
while True:
    sTime = time()
    frame = cam.capture_array()
    cv2.putText(frame, str(fps), (width, height), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
    cv2.rectangle(frame, (tl_x, tl_y), (br_x, br_y), (0,0,255), 3)
    cv2.imshow('camera', frame)
    if time() - xtime > .1:
        xtime = time()
        tl_x +=dx
        tl_y += dy
        br_x = tl_x+boxW
        br_y = tl_y+boxH

    print(tl_x, ' ', tl_y, ' ', br_x, ' ', br_y)

    if tl_x<0:
        dx = 5
    elif tl_y<0:
        dy = 5
    elif br_x>width-1:
        dx = -5
    elif br_y>359:
        dy = -5

    if cv2.waitKey(1) == ord('q'):
        break
    fps = 1/(sTime - time())

cv2.destroyAllWindows()