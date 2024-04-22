# plot bounding boxes on images with yolo format

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import random
import os

# Klasseninformationen

# 1. plot all BDD100 detection classes

'''
class_names = {
    0: 'pedestrian' ,
    1: 'rider' ,
    2: 'car' ,
    3: 'truck' ,
    4: 'bus',
    5: 'train' ,
    6: 'motorcycle' ,
    7: 'bicycle' ,
    8: 'traffic light' ,
    9: 'traffic sign'
}
'''

# 2. plot my classes I want to detect
'''
class_names = {
    0: 'pedestrian' ,
    1: 'rider' ,
    2: 'car' ,
    3: 'truck' ,
    4: 'bus',
    5: 'traffic light' ,
    6: 'traffic sign'
}
'''



class_names = {
    0: 'license-plate',
    1: 'car',  
    2: 'pedestrian',
    3: 'rider',
    4: 'truck',
    5: 'bus',
    6: 'traffic light',
    7: 'traffic sign'
}


def visualize_ground_truth(image_path, ground_truth_annotation_path, title):
    # Lade das Bild
    img = Image.open(image_path)

    # Neue Bildgröße festlegen (in Zoll)
    new_figsize = (20, 20)

    # Erstelle eine Figur und Achsen mit der neuen Bildgröße
    fig, ax = plt.subplots(1, figsize=new_figsize)

    plt.title(os.path.basename(title))

    # Zeige das Bild an
    ax.imshow(img)

    # Lade Ground Truth-Annotationen
    with open(ground_truth_annotation_path, 'r') as file:
        lines = file.readlines()

    # Legende für die Klassen initialisieren
    legend_elements = []

    


    ## for plots

    
    # Farbpalette für die Klassen erstellen
    '''   
    class_colors = {
        'pedestrian': 'b',
        'rider': 'r',
        'car': 'y',
        'truck': 'purple',
        'bus': 'green',
        'train': 'orange',
        'motorcycle': 'pink',
        'bicycle': 'cyan',
        'traffic light': 'magenta',
        'traffic sign': 'brown'
    }
    '''


    class_colors = {
        'license-plate': 'b',
        'car': 'r',  
        'pedestrian': 'y',
        'rider': 'purple',
        'truck': 'pink',
        'bus': 'orange',
        'traffic light': 'magenta',
        'traffic sign': 'brown'
    }
    
    
    '''
    class_colors = {
        'license-plate': 'b',
        'car': 'r'
    }
    '''

    # Durchlaufe die Annotationen und füge Rechtecke hinzu
    used_classes = set()  # Um zu überprüfen, ob eine Klasse bereits in der Legende ist
    for line in lines:
        data = line.split()
        # Annahme: Das Format ist "class x_center y_center width height"
        class_id, x_center, y_center, width, height = map(float, data)
        print('class id: ', class_id)
        # Konvertiere die Annotationen in Koordinaten
        x, y = x_center * img.width, y_center * img.height
        w, h = width * img.width, height * img.height
        # Klassenname
        class_name = class_names.get(int(class_id), f'Class {int(class_id)}')
        # Wähle die Farbe basierend auf der Klasse
        color = class_colors.get(class_name, 'gray')
        print('class name: ', class_name)
        print('color: ', color)
        # Überprüfe, ob die Klasse bereits in der Legende ist
        if class_name not in used_classes:
            # Füge das Patch-Objekt für die Legende hinzu
            legend_elements.append(patches.Patch(color=color, label=f'Class {int(class_id)}: {class_name}'))            
            # Markiere die Klasse als in der Legende verwendet
            used_classes.add(class_name)
        # Füge ein Rechteck für Ground Truth hinzu
        rect = patches.Rectangle((x - w / 2, y - h / 2), w, h, linewidth=2, edgecolor=color, facecolor='none')
        ax.add_patch(rect)

        # Füge die Klassenbezeichnung als Text hinzu
        ax.text(x - w / 2, y - h / 2, f'{class_name}', fontsize=10, color=color)
    # Füge eine Legende hinzu
    ax.legend(handles=legend_elements, loc='upper right')
    # Zeige das Bild mit Ground Truth an
    plt.show()



# Pfade zu den Bildern und Labels
#image_folder = '/home/krones2/Schreibtisch/Experiment2/LicensePlateOriginal/train/images'
#gt_folder =  '/home/krones2/Schreibtisch/Experiment2/LicensePlateOriginal/train/labels'


image_folder = '/home/krones2/Schreibtisch/Experiment2/bdd100knewsmall/train/images'
gt_folder =  '/home/krones2/Schreibtisch/Experiment2/bdd100knewsmall/train/labels'




# Plot 5 random images with labels
image_files = os.listdir(image_folder)
gt_files = os.listdir(gt_folder)

# Zufällige Auswahl von 10 Bildern
random_image_files = random.sample(image_files, 10)

#print('random_image_files: ', random_image_files)
gt_files = [f.replace('.jpg', '.txt') for f in random_image_files]

#print('gt_files: ', gt_files)

for image_file, gt_file in zip(random_image_files, gt_files):
    image= image_folder+'/'+image_file
    gt = gt_folder+'/'+gt_file
    print(image)
    print(gt)
    visualize_ground_truth(image, gt, title=image_file)



# Plot specific image 
'''
# Plot 1 specific image with labels
    
image_file = "/home/krones2/Schreibtisch/Experiment2/LicensePlateOriginal/images/0a0a0b1a-7c39d841.jpg"  # Name des gewünschten Bildes
gt_file = "/home/krones2/Schreibtisch/Experiment2/LicensePlateOriginal/labels/0a0a0b1a-7c39d841.txt"  # Name des entsprechenden Labels

image_path = os.path.join(image_folder, image_file)
gt_path = os.path.join(gt_folder, gt_file)
visualize_ground_truth(image_path, gt_path, title=image_file)
'''