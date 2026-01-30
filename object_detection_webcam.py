"""
Object Detection - Webcam
==========================
Description: TensorFlow Lite object detection using standard USB webcam instead of Pi Camera. 
EfficientDet model detects objects with configurable score thresholds.

Hardware Requirements:
- USB Webcam
- TFLite model file (efficientdet_lite0.tflite)

Features: Webcam support, object detection, visualization utilities

Author: Vilas
"""

import cv2
import time
# from picamera2 import Picamera2
from  tflite_support.task import core, processor, vision
import utils

model = 'efficientdet_lite0.tflite'
num_threads = 4

width =640
height = 360

# cam = cv2.VideoCapture(0)
# cam.preview_configuration.main.size = (width, height)
# cam.preview_configuration.main.format = 'RGB888'
# cam.preview_configuration.align()
# cam.configure("preview")
# cam.start()

webCam = '/dev/video19'
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)

pos = (20, 60)
font = cv2.FONT_HERSHEY_SIMPLEX
height=1.5
weight=3
myColor = (255, 0, 0)

fps = 0

base_option=core.BaseOptions(file_name=model, use_coral=False, num_threads = num_threads)
detection_options = processor.DetectionOptions(max_results=8, score_threshold=.3)
options=vision.ObjectDetectorOptions(base_options=base_option, detection_options = detection_options)
detector = vision.ObjectDetector.create_from_options(options)

import os

# Get the folder where THIS script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Join it with the model name
model_path = os.path.join(script_dir, 'efficientdet_lite0.tflite')

# Update your BaseOptions to use 'model_path' instead of just the string
base_option = os.core.BaseOptions(file_name=model_path, use_coral=False, num_threads=num_threads)

while True:
    tstart = time.time()
    ret, im = cam.read()
    im = cam.capture_array()
    imRGB = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    detects1=detector.detect(imTensor)
    print(detects1)
    print()
    # image=utils.visualize(im, detects1) #this detects everything

    imTensor=vision.TensorImage.create_from_array(imRGB)
    cv2.putText(im, fps, pos, font, height, myColor, weight)
    im = cv2.flip(im, -1)
    cv2.imshow('camera', im)
    if cv2.waitKey(1)==ord('q'):
        break

    fps = 1/(time.time() - tstart)

cv2.destroyAllWindows()