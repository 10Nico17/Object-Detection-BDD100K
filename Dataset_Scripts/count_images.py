# check that images match label files

import os
import json

def count_jpg_files(folder_path):
    jpg_count = 0
    for file in os.listdir(folder_path):
        if file.endswith(".jpg"):
            jpg_count += 1
    return jpg_count  


def count_linked_jpg_files(json_file):
    jpg_count = 0
    with open(json_file, 'r') as f:
        data = json.load(f)
        for item in data:
            if item["name"].endswith('.jpg'):
                jpg_count += 1
    return jpg_count



folder_path_train = "/home/krones2/Schreibtisch/Yolo/images/train"  # Hier den Pfad zum Zielordner angeben
folder_path_val = "/home/krones2/Schreibtisch/Yolo/images/val"  # Hier den Pfad zum Zielordner angeben
jpg_count_train = count_jpg_files(folder_path_train)
jpg_count_val = count_jpg_files(folder_path_val)


print("Count JPG-Files image train folder:", jpg_count_train)
print("Count JPG-Files image val folder:", jpg_count_val)


json_file_train = "/home/krones2/Schreibtisch/Yolo/labels/train/det_train.json"  # Pfad zur JSON-Datei
json_file_val = "/home/krones2/Schreibtisch/Yolo/labels/val/det_val.json"

jpg_count_labels_train = count_linked_jpg_files(json_file_train)
jpg_count_labels_val = count_linked_jpg_files(json_file_val)



print("Count JPG-Files train JSON-File:", jpg_count_labels_train)
print("Count JPG-Files val JSON-File:", jpg_count_labels_val)


