from ultralytics import YOLO
import os
import random
import cv2
from PIL import Image

# Load a model
model = YOLO('best.pt')

# Customize validation settings
validation_results = model.val(data='dataset5.yaml')

print('Confusion matrix: ', validation_results.confusion_matrix.matrix)




