# OpenCV Computer Vision Projects

Computer vision and image processing projects using OpenCV, Picamera2, and TensorFlow Lite on Raspberry Pi. Real-time face detection, object tracking, color-based tracking, and servo-controlled camera systems.

## 📋 Project List

| Script | Description |
|--------|-------------|
| **face_detection.py** | Real-time face detection using Haar Cascade classifier |
| **face_eye_detection.py** | Simultaneous face and eye detection with bounding boxes |
| **bouncing_box_animation.py** | Animated bouncing box on live camera feed |
| **hsv_color_filter.py** | HSV color space filtering and object masking |
| **color_detection_trackbars.py** | Color detection with trackbar controls for HSV tuning |
| **image_array_manipulation.py** | Direct pixel array manipulation demo |
| **object_detection_tflite.py** | TensorFlow Lite object detection (EfficientDet) |
| **object_detection_webcam.py** | Object detection using standard webcam |
| **pan_tilt_tracking.py** | Servo-controlled pan-tilt color tracking system |
| **servo_color_tracking.py** | Advanced servo tracking with HSV filtering |
| **basic_picamera.py** | Basic Picamera2 setup with overlays |
| **interactive_trackbars.py** | Interactive rectangle positioning with trackbars |
| **utils.py** | TensorFlow Lite visualization utilities |
| **estest.py** | Path configuration utility for TFLite models |

## 🔧 Hardware Requirements

- Raspberry Pi 4 (or compatible model)
- Raspberry Pi Camera Module (v2 or HQ)
- Pan-Tilt servo mechanism (for tracking projects)
- 2x Servo motors (GPIO 11, 13)

## 📦 Dependencies

```bash
# System packages
sudo apt-get update
sudo apt-get install python3-opencv python3-picamera2

# Python packages
pip3 install opencv-python
pip3 install picamera2
pip3 install tflite-support
pip3 install tflite-runtime
pip3 install piservo
```

## 📁 Data Files

The `data/` folder contains Haar Cascade XML classifiers:
- Face detection (frontal, profile)
- Eye detection
- Full body detection
- License plate detection
- And more...

## 🚀 Usage

### Basic Camera Test
```bash
python3 basic_picamera.py
```

### Face Detection
```bash
python3 face_detection.py
```

### Color Tracking with Servos
```bash
python3 servo_color_tracking.py
```

### Object Detection
```bash
python3 object_detection_tflite.py
```

Press 'q' to quit most applications.

## 🎯 Key Features

- **Real-time Processing**: Optimized for 30-40 FPS on Raspberry Pi
- **FPS Display**: All projects show live frame rate
- **Haar Cascades**: Pre-trained classifiers for face/eye detection
- **HSV Tracking**: Robust color-based object tracking
- **TensorFlow Lite**: Efficient neural network inference
- **Servo Control**: Automated camera tracking systems
- **Interactive Tuning**: Trackbar interfaces for parameter adjustment

## 📝 Project Details

### Face Detection Projects
- Uses pre-trained Haar Cascade classifiers
- Real-time bounding box visualization
- Optimized for Raspberry Pi Camera

### Color Tracking Projects
- HSV color space for robust tracking
- Interactive trackbar parameter tuning
- Servo integration for autonomous tracking

### Object Detection
- TensorFlow Lite EfficientDet model
- Multi-object detection support
- Configurable confidence thresholds

## ⚠️ Notes

- Ensure camera is enabled: `sudo raspi-config`
- Adjust camera resolution based on Pi model
- Servo projects require proper power supply
- TFLite models should be in the same directory

## 👤 Author

Vilas - Computer Vision & Robotics Enthusiast
