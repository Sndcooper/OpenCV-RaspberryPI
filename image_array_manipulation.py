"""
Image Array Manipulation
========================
Description: Direct pixel array manipulation demo. Modifies specific pixel regions by directly 
setting RGB values in the frame array. Demonstrates low-level image processing.

Hardware Requirements:
- Raspberry Pi Camera Module

Features: Direct pixel access, array manipulation, FPS display

Author: Vilas
"""

from picamera2 import Picamera2
from time import time
import cv2

cam = Picamera2()
width = 720
height = 360
cam.preview_configuration.main.size = (width, height)
cam.preview_configuration.main.format = 'RGB888'
cam.preview_configuration.align()

cam.configure('preview')
cam.start()

fps = 0
pos = (15, 60)
color = (100, 100, 100)
thickness = 3
height = 1

while True:
    sTime = time()
    frame = cam.capture_array()
    frame[20:100, 50:70] = [100, 100, 100]
    cv2.putText(frame, str(int(fps)), pos, cv2.FONT_HERSHEY_SIMPLEX, height, color, thickness)
    cv2.imshow('he', frame)
    if cv2.waitKey(1) == ord('q'):
        break

    fps = 1/(time()-sTime)

cv2.destroyAllWindows()