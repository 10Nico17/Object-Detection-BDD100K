# Split the big BDD100K dataset into a smaller set and divide it into train/val/test

import os
import random
import shutil

def split_dataset(image_dir, label_dir, output_dir, num_images, train_ratio, val_ratio, test_ratio):
    # Erstelle Verzeichnisse für Trainings-, Validierungs- und Testdaten
    train_dir = os.path.join(output_dir, 'train')
    val_dir = os.path.join(output_dir, 'val')
    test_dir = os.path.join(output_dir, 'test')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Erstelle Unterordner für Bilder und Labels in Trainings-, Validierungs- und Testverzeichnissen
    for subdir in ['images', 'labels']:
        os.makedirs(os.path.join(train_dir, subdir), exist_ok=True)
        os.makedirs(os.path.join(val_dir, subdir), exist_ok=True)
        os.makedirs(os.path.join(test_dir, subdir), exist_ok=True)

    # Liste aller Bilddateien im Bildverzeichnis erstellen
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]

    # Zufällige Auswahl einer Teilmenge von Bilddateien
    selected_images = random.sample(image_files, num_images)

    # Anzahl der Bilder für jeden Satz berechnen
    num_train = int(num_images * train_ratio)
    num_val = int(num_images * val_ratio)
    num_test = int(num_images * test_ratio)

    # Zufällige Auswahl der Bilder für Trainings-, Validierungs- und Testdaten
    random.shuffle(selected_images)
    train_images = selected_images[:num_train]
    val_images = selected_images[num_train:num_train + num_val]
    test_images = selected_images[num_train + num_val:num_train + num_val + num_test]

    # Kopieren der ausgewählten Bilder in die entsprechenden Verzeichnisse und die dazugehörigen Labeldateien
    for img_file in train_images:
        shutil.copy(os.path.join(image_dir, img_file), os.path.join(train_dir, 'images', img_file))
        shutil.copy(os.path.join(label_dir, img_file.replace('.jpg', '.txt')), os.path.join(train_dir, 'labels', img_file.replace('.jpg', '.txt')))
    for img_file in val_images:
        shutil.copy(os.path.join(image_dir, img_file), os.path.join(val_dir, 'images', img_file))
        shutil.copy(os.path.join(label_dir, img_file.replace('.jpg', '.txt')), os.path.join(val_dir, 'labels', img_file.replace('.jpg', '.txt')))
    for img_file in test_images:
        shutil.copy(os.path.join(image_dir, img_file), os.path.join(test_dir, 'images', img_file))
        shutil.copy(os.path.join(label_dir, img_file.replace('.jpg', '.txt')), os.path.join(test_dir, 'labels', img_file.replace('.jpg', '.txt')))


image_dir = '/home/krones2/Schreibtisch/Experiment2/bdd100knew/images'        # Verzeichnis mit Bildern
label_dir = '/home/krones2/Schreibtisch/Experiment2/bdd100knew/labels'        # Verzeichnis mit Labels im YOLO-Format

output_dir = '/home/krones2/Schreibtisch/Experiment2/bdd100knewsmall/'              # Ausgabeverzeichnis für Trainings-, Validierungs- und Testdaten

num_images_to_use = 30000               # Anzahl der Bilder aus dem Gesamtdatensatz, die verwendet werden sollen
train_ratio = 0.7                       # Anteil der Trainingsdaten
val_ratio = 0.15                        # Anteil der Validierungsdaten
test_ratio = 0.15                       # Anteil der Testdaten

split_dataset(image_dir, label_dir, output_dir, num_images_to_use, train_ratio, val_ratio, test_ratio)
