# convert BDD100K format to YOLO format and check borders 

import os
import json
from PIL import Image
import shutil

no_labels = []
ignored_classes = []
number_images = 0


def convert_to_yolo(labels, image_width, image_height):
    yolo_labels = []
    for label in labels:
        class_name = label['category']
        if class_name in class_names:
            class_id = class_names[class_name]
            x_center = (label['box2d']['x1'] + label['box2d']['x2']) / (2 * image_width)
            y_center = (label['box2d']['y1'] + label['box2d']['y2']) / (2 * image_height)
            width = (label['box2d']['x2'] - label['box2d']['x1']) / image_width
            height = (label['box2d']['y2'] - label['box2d']['y1']) / image_height
            
            # Koordinaten und Dimensionen auf 1.0 begrenzen, wenn sie größer sind
            if x_center > 1.1 or y_center > 1.1 or width > 1.1 or height > 1.1:
                print(f"Error: Label for category '{class_name}' in image '{image_name}' has invalid coordinates or dimensions.")
            else:
                x_center = min(max(x_center, 0), 1)
                y_center = min(max(y_center, 0), 1)
                width = min(width, 1)
                height = min(height, 1)
                yolo_labels.append((class_id, x_center, y_center, width, height))
        else:
            if class_name not in ignored_classes:
                ignored_classes.append(class_name)
    return yolo_labels


def main(json_file_path, image_folder, output_folder):
    global number_images 
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    
    for entry in data:
        image_name = entry['name']
        number_images += 1
        image_path = os.path.join(image_folder, image_name)
        image = Image.open(image_path)
        image_width, image_height = image.size
        
        labels = entry.get('labels', [])  # Labels abrufen oder leere Liste verwenden, wenn keine vorhanden sind
        
        yolo_labels = convert_to_yolo(labels, image_width, image_height)
        #print('yolo_labels: ', yolo_labels)
    
        if len(yolo_labels) == 0:
            no_labels.append(image_name)  
        else:
            txt_file_path = os.path.join(output_folder, os.path.splitext(image_name)[0] + '.txt')
            with open(txt_file_path, 'w') as f:
                if not yolo_labels:  # Überprüfen, ob Labels vorhanden sind
                    pass
                else:
                    for label in yolo_labels:
                        line = ' '.join(map(str, label))
                        f.write(line + '\n')    
                    # Kopieren Sie das Bild in den output_folder2 (yolo_subset_images), wenn Labels vorhanden sind
                    print('Copy Image')
                    output_image_path = os.path.join(output_folder2, image_name)
                    shutil.copy(image_path, output_image_path) 
        
        
        '''
        txt_file_path = os.path.join(output_folder, os.path.splitext(image_name)[0] + '.txt')


        with open(txt_file_path, 'w') as f:
            if not yolo_labels:  # Überprüfen, ob Labels vorhanden sind
                pass
            else:
                for label in yolo_labels:
                    line = ' '.join(map(str, label))
                    f.write(line + '\n')
        
        '''

        # Erstelle eine leere Textdatei, wenn keine Labels vorhanden sind
        #if not os.path.exists(txt_file_path):          
            #with open(txt_file_path, 'w'):
                #pass


if __name__ == "__main__":
    

    class_names = {
        'license-plate': 0,
        'car': 1,  
        'pedestrian': 2,
        'rider': 3,
        'truck': 4,
        'bus': 5,
        'traffic light': 6,
        'traffic sign': 7
    }

    json_file_path = 'labels/train/det_train.json'
    image_folder = 'images/train'


    output_folder = '/home/krones2/Schreibtisch/Experiment2/bdd100k/labels'
    output_folder2 = '/home/krones2/Schreibtisch/Experiment2/bdd100k/images'


    main(json_file_path, image_folder, output_folder)
    print('ignored_classes: ', ignored_classes)
    print('number_images: ', number_images)
    #print('no_labels: ', no_labels)
