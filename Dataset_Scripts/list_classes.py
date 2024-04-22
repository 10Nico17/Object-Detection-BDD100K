# list the classes in the dataset and plot

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image


def visualize_ground_truth(image_path, ground_truth_annotation_path, title):
    # Lade das Bild
    img = Image.open(image_path)

    # Neue Bildgröße festlegen (in Zoll)
    new_figsize = (20, 20)

    # Erstelle eine Figur und Achsen mit der neuen Bildgröße
    fig, ax = plt.subplots(1, figsize=new_figsize)

    # Setze den Titel des Bildes
    plt.title(title)

    # Zeige das Bild an
    ax.imshow(img)

    # Lade Ground Truth-Annotationen
    with open(ground_truth_annotation_path, 'r') as file:
        lines = file.readlines()

    # Legende für die Klassen initialisieren
    legend_elements = []

    # Farbpalette für die Klassen erstellen
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

    # Durchlaufe die Annotationen und füge Rechtecke hinzu
    used_classes = set()  # Um zu überprüfen, ob eine Klasse bereits in der Legende ist
    for line in lines:
        data = line.split()

        # Annahme: Das Format ist "class x_center y_center width height"
        class_id, x_center, y_center, width, height = map(float, data)

        # Konvertiere die Annotationen in Koordinaten
        x, y = x_center * img.width, y_center * img.height
        w, h = width * img.width, height * img.height

        # Klassenname
        class_name = class_names.get(int(class_id), f'Class {int(class_id)}')

        # Wähle die Farbe basierend auf der Klasse
        color = class_colors.get(class_name, 'gray')

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

# Ordnerpfad mit den Textdateien
folder_path = 'labels_to_yolo'

# Bilderpfad
image_folder_path = 'images/train'

# Klasseninformationen
class_names = {
    0: 'pedestrian',
    1: 'rider',
    2: 'car',
    3: 'truck',
    4: 'bus',
    5: 'train',
    6: 'motorcycle',
    7: 'bicycle',
    8: 'traffic light',
    9: 'traffic sign'
}


# Erstellen eines leeren Pandas DataFrame
df = pd.DataFrame(columns=['Image'] + list(class_names.values()))

# Durchlaufe alle Textdateien im Ordner
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        image_name = os.path.splitext(filename)[0] + '.jpg'
        image_path = os.path.join(image_folder_path, image_name)
        
        # Initialisiere eine Liste, um die Anzahl jeder Klasse für das Bild zu speichern
        class_counts = [0] * len(class_names)
        
        with open(os.path.join(folder_path, filename), 'r') as file:
            lines = file.readlines()
            for line in lines:
                class_id = int(line.split()[0])
                if class_id in class_names:
                    class_counts[class_id] += 1
        
        # Füge eine Zeile zum DataFrame hinzu
        df.loc[len(df)] = [image_name] + class_counts

# Anzeigen des erstellten DataFrame
print(df)


most_objects_per_class = []

# Gruppieren des DataFrames nach jeder Klasse und Finden der Bilder mit den meisten Objekten für jede Klasse
for class_name in class_names.values():
    # Gruppieren nach der aktuellen Klasse und Summieren der Anzahl von Objekten
    class_group = df.groupby('Image')[class_name].sum()
    
    # Sortieren der Gruppe nach Anzahl der Objekte absteigend und Auswahl der ersten drei Bilder
    top_three_images = class_group.sort_values(ascending=False).index[:3]
    
    # Hinzufügen der drei Bilder mit den meisten Objekten zur Liste
    for image in top_three_images:
        most_objects_per_class.append((class_name, image))

# Anzeigen der Liste der Bilder mit den meisten Objekten für jede Klasse
for class_name, image in most_objects_per_class:
    #print(f"Klasse: {class_name}, Bild mit den meisten Objekten: {image}")
    image_folder = 'images/train'
    gt_folder = 'labels_to_yolo'
    image_path = image_folder+'/'+image
    #print('image_path: ', image_path)
    txt_path = image.replace(".jpg", ".txt")
    gt_path = gt_folder+'/'+txt_path
    #print('gt_path: ', gt_path)
    
    #ground_truth_path = gt_folder+

    title = class_name+' :'+ image


    visualize_ground_truth(image_path, gt_path, title)


# Klassen nach der Anzahl der Objekte in den Bildern sortieren
#sorted_df = df.sort_values(by='train', ascending=False)

# DataFrame filtern, um nur die Zeilen mit train >= 1 zu behalten
filtered_df = df[df['train'] >= 1]

# Anzeigen des neuen DataFrames
print(filtered_df)


#head(10).

# Durchlaufe die einzelnen Reihen und drucke den Bildnamen
for index, row in filtered_df.iterrows():
    image_name = row['Image']
    image_folder = 'images/train'
    gt_folder = 'labels_to_yolo'
    image_path = image_folder+'/'+image_name
    txt_path = image_name.replace(".jpg", ".txt")
    gt_path = gt_folder+'/'+txt_path
    titel = 'train: '+image_name
    visualize_ground_truth(image_path, gt_path, titel)


