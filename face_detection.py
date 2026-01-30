"""
Face Detection
==============
Description: Real-time face detection using Haar Cascade classifier with Picamera2. Detects faces 
in video stream and draws bounding boxes with live FPS counter.

Hardware Requirements:
- Raspberry Pi Camera Module
- Haar Cascade XML file (haarcascade_frontalface_default.xml)

Features: Face detection, bounding boxes, FPS display

Author: Vilas
"""

import cv2
from picamera2 import Picamera2
from time import time, sleep
piCam = Picamera2() #object
piCam.preview_configuration.main.size=(720, 360)
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

faceCas = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')

while True:
    stime = time()
    frame=piCam.capture_array()
    frame = cv2.flip(frame, -1)
    frameGrey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCas.detectMultiScale(frameGrey, 1.3, 5)
    print(faces)
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(frame, str(int(fps)), pos,font, height, myColor, weight)
    cv2.imshow("piCam", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    etime = time()
    dtime = etime - stime
    fps = .9*fps + .1*1/dtime
    # print(int(fps))
cv2.destroyAllWindows()
