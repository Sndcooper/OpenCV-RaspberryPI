"""
Basic Picamera Setup
====================
Description: Basic Picamera2 configuration with shape overlays. Displays live camera feed with 
rectangle and circle overlays, demonstrating fundamental OpenCV drawing functions and FPS calculation.

Hardware Requirements:
- Raspberry Pi Camera Module

Features: Camera setup, shape overlays, FPS display, pixel value inspection

Author: Vilas
"""

import cv2
from picamera2 import Picamera2
from time import time, sleep
piCam = Picamera2() #object
piCam.preview_configuration.main.size=(1280, 720)
piCam.preview_configuration.main.format="RGB888" 
piCam.preview_configuration.controls.FrameRate=40
# piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()

#for fps
fps = 0
pos = (15, 40)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1
myColor = (255, 0, 0) #BGR
weight = 2

#for rectangle
upperLeft = (250, 50)
lowerRight = (1050, 600)
rColor = (0, 0, 0)
thickness = 4

#for circle
cent = (640, 360)
r = 40
cColor = (0,255,255)
cthick = -1

while True:
    stime = time()
    frame=piCam.capture_array()
    print(frame[0, 0])
    cv2.putText(frame, str(int(fps)), pos,font, height, myColor, weight)
    cv2.rectangle(frame, upperLeft, lowerRight, rColor, thickness)
    cv2.circle(frame, cent, r, cColor, cthick)
    cv2.imshow("piCam", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    etime = time()
    dtime = etime - stime
    fps = .9*fps + .1*1/dtime
    # print(int(fps))
cv2.destroyAllWindows()
