"""
Path Configuration Utility
===========================
Description: Utility script for configuring TensorFlow Lite model paths. Ensures model files are 
loaded from script directory regardless of execution location.

Usage: Import and use for dynamic model path resolution

Author: Vilas
"""

import os

# Get the folder where THIS script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Join it with the model name
model_path = os.path.join(script_dir, 'efficientdet_lite0.tflite')

# Update your BaseOptions to use 'model_path' instead of just the string
base_option = os.core.BaseOptions(file_name=model_path, use_coral=False, num_threads=num_threads)