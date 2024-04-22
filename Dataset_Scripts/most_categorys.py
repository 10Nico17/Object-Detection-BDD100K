import json

# Pfad zur JSON-Datei mit den Bildinformationen
json_file_path = '/home/krones2/Schreibtisch/Yolo/labels/train/det_train.json'

# Laden der JSON-Datei
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Dictionary zur Zählung der Kategorien für jeden Bildnamen initialisieren
category_counts = {}

# Durchlaufe die Daten und zähle die Kategorien für jeden Bildnamen
for item in data:
    if 'labels' in item:  # Überprüfen, ob der Schlüssel 'labels' vorhanden ist
        image_name = item['name']
        categories = set(label['category'] for label in item['labels'])
        category_counts[image_name] = len(categories)

# Finde den Bildnamen mit den meisten unterschiedlichen Kategorien
if category_counts:
    max_categories_image = max(category_counts, key=category_counts.get)
    max_categories_count = category_counts[max_categories_image]

    print(f"Bild mit den meisten unterschiedlichen Kategorien: {max_categories_image}")
    print(f"Anzahl der unterschiedlichen Kategorien: {max_categories_count}")
else:
    print("Keine Daten vorhanden oder keine Labels gefunden.")