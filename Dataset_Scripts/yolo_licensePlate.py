from ultralytics import YOLO
import os
import random
import cv2
from PIL import Image

# Create a new YOLO model from scratch
model = YOLO('yolov8n.yaml')

# Load a pretrained YOLO model (recommended for training from the BDD100K model
model = YOLO('/home/krones2/Schreibtisch/Google Colab/YOLOv8s/second 15 episodes/best.pt')

# Train the model using the 'coco128.yaml' dataset for 10 episodes
results = model.train(data='/home/krones2/Schreibtisch/Licenseoriginal/data.yaml', epochs=10)


# Verzeichnis mit Bildern
images_dir = '/home/krones2/Schreibtisch/Licenseoriginal/test/images/'

# Liste der Dateien im Verzeichnis
image_files = os.listdir(images_dir)

# Zufällige Auswahl von fünf Bildern
random_images = random.sample(image_files, 10)

# Für jedes ausgewählte Bild
for image_file in random_images:
    # Pfad zum Bild
    image_path = os.path.join(images_dir, image_file)

    # Laden des Bildes
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Vorhersage mit dem Modell
    results = model(image_path,save=True)