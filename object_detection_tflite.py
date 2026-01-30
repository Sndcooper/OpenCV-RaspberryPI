"""
Object Detection - TensorFlow Lite
===================================
Description: Real-time object detection using TensorFlow Lite EfficientDet model. Detects multiple 
objects with confidence scores using optimized neural network inference.

Hardware Requirements:
- Raspberry Pi Camera Module
- TFLite model file (efficientdet_lite0.tflite)

Features: Multi-object detection, confidence thresholds, real-time inference

Author: Vilas
"""

import cv2
import time
from picamera2 import Picamera2
from  tflite_support.task import core, processor, vision
import utils

model = 'efficientdet_lite0.tflite'
num_threads = 4

width =640
height = 360

cam = Picamera2()
cam.preview_configuration.main.size = (width, height)
cam.preview_configuration.main.format = 'RGB888'
cam.preview_configuration.align()
cam.configure("preview")
cam.start()

webCam = '/dev/video19'
cam1=cv2.VideoCapture(cam)
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