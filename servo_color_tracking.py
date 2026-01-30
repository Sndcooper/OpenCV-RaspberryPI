"""
Servo Color Tracking
====================
Description: Advanced color tracking with servo-controlled camera. Detects colored objects using HSV 
filtering, calculates centroids, and controls pan-tilt servos to keep object centered in frame.

Hardware Requirements:
- Raspberry Pi Camera Module
- Pan servo on GPIO 13
- Tilt servo on GPIO 11

Features: Centroid tracking, PID-like control, HSV filtering, contour detection, servo automation

Author: Vilas
"""

from picamera2 import Picamera2
from time import time
import cv2
import numpy as np
from piservo import Servo

lHue=0
lSat=0
lVal=0
hHue=0
hSat=0
hVal=0

pan = Servo(gpio = 13)
tilt = Servo(gpio = 11)

pana=0
tilta=0

pan.write(pana)
pan.write(tilta)
def LHue(val):
    global lHue
    lHue = val

def HHue(val):
    global hHue
    hHue = val

def LSat(val):
    global lSat
    lSat = val

def HSat(val):
    global hSat
    hSat = val

def LVal(val):
    global lVal
    lVal = val

def HVal(val):
    global hVal
    hVal = val

def traintrack(val):
    global train
    train=val

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

cv2.createTrackbar('LHue', 'mytrackbar', 80, 255, LHue)
cv2.createTrackbar('HHue', 'mytrackbar', 140, 255, HHue)

cv2.createTrackbar('LSat', 'mytrackbar', 40, 255, LSat)
cv2.createTrackbar('HSat', 'mytrackbar', 200, 255, HSat)

cv2.createTrackbar('LVal', 'mytrackbar', 0, 255, LVal)
cv2.createTrackbar('HVal', 'mytrackbar', 69, 255, HVal)

cv2.createTrackbar('train', 'mytrackbar', 0, 1, traintrack)

lowerBound = np.array([lHue, lSat, lVal])
upperBound = np.array([hHue, hSat, hVal])

while True:

    lowerBound = np.array([lHue, lSat, lVal])
    upperBound = np.array([hHue, hSat, hVal])
    sTime = time()
    frame = cam.capture_array()
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(frameHSV, lowerBound, upperBound)
    mymask = cv2.resize(mask, (200, 100))
    object = cv2.bitwise_and(frame, frame, mask=mask)
    object1 = cv2.resize(object, (350, 180))

    contours, junk = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours)>0:
        contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse = True)
        cv2.drawContours(frame,contours,  -1, (255, 0, 0), 3)
        contour = contours[0]
        x, y, w, h =cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)
        error = (x+w/2)-width/2
        tilterror = (y+h/2) -height/2
        pana = pana-error/70
        if pana>90:
            pana=90
        if pana<-90:
            pana=-90
        if abs(error)>30 and train ==1:
            pan.write(pana)
        tilta = tilta-error/70
        if tilta>90:
            tilta=90
        if tilta<-90:
            tilta = -90
        if abs(tilterror)>30 and train ==1:
            tilt.write(tilta)

    cv2.putText(frame, str(int(fps)), fpspos, cv2.FONT_HERSHEY_SIMPLEX, fpsheight, fpscolor, fpsthickness)
    cv2.imshow('he', frame)

    cv2.imshow('mask', mymask)
    cv2.imshow('object', object1)

    if cv2.waitKey(1) == ord('q'):
        break

    fps = 1/(time()-sTime)

cv2.destroyAllWindows()