import json
import os
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Pfad zur JSON-Datei mit den Bildinformationen
json_file_path = 'labels/train/det_train.json'


# Pfad zum Ordner mit den Bildern
image_folder_path = 'images/train'

# Laden der JSON-Datei
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Zufällige Auswahl von fünf Bildern
random_images = random.sample(data, 5)

# Funktion zum Zeichnen der Bounding-Boxen
def draw_boxes(image_path, labels):
    # Lade das Bild
    img = Image.open(image_path)
    plt.imshow(img)


    # Legende für die Klassen initialisieren
    legend_elements = []
    used_classes = set()  # Um zu überprüfen, ob eine Klasse bereits in der Legende ist

    # Farbpalette für die Klassen erstellen
    class_colors = {
        'pedestrian': 'b',
        'rider': 'r',
        'car': 'y',
        'truck': 'purple',
        'bus': 'green',
        'traffic light': 'magenta',
        'traffic sign': 'brown'
    }

    # Durchlaufe die Labels und zeichne die Bounding-Boxen
    for label in labels:
        category = label['category']
        print('category: ', category)
        box = label['box2d']
        x1, y1, x2, y2 = box['x1'], box['y1'], box['x2'], box['y2']
        width, height = x2 - x1, y2 - y1

        # Farbe basierend auf der Klasse auswählen
        color = class_colors.get(category, 'gray')

        # Überprüfe, ob die Klasse bereits in der Legende ist
        if category not in used_classes:
            # Füge das Patch-Objekt für die Legende hinzu
            legend_elements.append(patches.Patch(color=color, label=f'{category}'))
            # Markiere die Klasse als in der Legende verwendet
            used_classes.add(category)

        # Zeichne die Bounding-Box
        rect = patches.Rectangle((x1, y1), width, height, linewidth=1, edgecolor=color, facecolor='none')
        plt.gca().add_patch(rect)

        # Füge die Klassenbezeichnung als Text hinzu
        plt.text(x1, y1 - 5, category, fontsize=8, color=color)

    # Füge eine Legende hinzu
    plt.legend(handles=legend_elements, loc='upper right')

    # Setze den Titel des Plots auf den Bildnamen
    plt.title(os.path.basename(image_path))

    # Zeige das Bild mit Bounding-Boxen an
    plt.show()





'''
# Durchlaufe die ausgewählten Bilder
for image_info in random_images:
    image_name = image_info['name']
    image_path = os.path.join(image_folder_path, image_name)
    labels = image_info['labels']

    # Plotte das Bild mit Bounding-Boxen
    draw_boxes(image_path, labels)
'''


# Manuell vorgegebener Bildpfad
specified_image_path = '/home/krones2/Schreibtisch/Yolo/images/train/97ebca09-17e21801.jpg'

# Suche den vorgegebenen Bildpfad in der JSON-Datei
for item in data:
    image_name = item['name']
    if image_name == os.path.basename(specified_image_path):
        labels = item['labels']  # Extrahiere die Labels für dieses Bild
        draw_boxes(specified_image_path, labels)
        break
else:
    print("Das vorgegebene Bild wurde nicht in der JSON-Datei gefunden.")