"""
HSV Color Filter
================
Description: HSV color space filtering for object isolation. Creates mask based on HSV thresholds, 
displays original, mask, and filtered object views. Shows pixel HSV values at center.

Hardware Requirements:
- Raspberry Pi Camera Module

Features: HSV conversion, color masking, multi-window display, pixel inspection

Author: Vilas
"""

from picamera2 import Picamera2
from time import time
import cv2
import numpy as np

cam = Picamera2()
width = 720
height = 360

cam.preview_configuration.main.size = (width, height)
cam.preview_configuration.main.format = 'RGB888'
cam.preview_configuration.align()

cam.configure('preview')
cam.start()



fps = 0
pos = (15, 45)
color = (255, 255, 255)
thickness = 2
height = 1

hueLow=-150
hueHigh = 190

saturationLow = 55
saturationHigh = 110

valueLow = 80
valueHigh = 130

lowerBound = np.array([hueLow, saturationLow, valueLow])
upperBound = np.array([hueHigh, saturationHigh, valueHigh])
#20-40 20-40 150-180

while True:
    tstart = time()
    frame = cam.capture_array()
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.rectangle(frame, (355,175), (365,185), (255,0,0), 1)

    mask = cv2.inRange(frameHSV, lowerBound, upperBound)
    mymask = cv2.resize(mask, (200, 100))
    object = cv2.bitwise_and(frame, frame, mask=mask)
    object1 = cv2.resize(object, (350, 180))
    print(frameHSV[180,360])
    cv2.putText(frame, str(int(fps)), pos, cv2.FONT_HERSHEY_SIMPLEX, height, color, thickness)
    cv2.imshow('h', frame)
    cv2.imshow('mask', mymask)
    cv2.imshow('object', object1)
    if cv2.waitKey(1) == ord('q'):
        break
    
    fps = 1/(time()-tstart)

cv2.destroyAllWindows()