# Control dataset after transform format


import json

# Pfad zur JSON-Datei
#json_file_path = 'labels/train/det_train.json'
json_file_path = 'labels/val/det_val.json'

# Zähler für .jpg-Dateien initialisieren
jpg_count = 0

# JSON-Datei öffnen und Daten laden
with open(json_file_path, 'r') as f:
    data = json.load(f)

# Durch jeden Eintrag in der JSON-Datei iterieren
for entry in data:
    # Überprüfen, ob der Eintrag ein Bild ist (Endung mit .jpg)
    if entry['name'].endswith('.jpg'):
        # Wenn ja, Zähler erhöhen
        jpg_count += 1

# Initialisieren der Zähler für jede Klasse
class_counts = {
    'pedestrian': 0,
    'rider': 0,
    'car': 0,
    'truck': 0,
    'bus': 0,
    'train': 0,
    'motorcycle': 0,
    'bicycle': 0,
    'traffic light': 0,
    'traffic sign': 0
}

# JSON-Datei öffnen und Daten laden
with open(json_file_path, 'r') as f:
    data = json.load(f)

# Durch jeden Eintrag in der JSON-Datei iterieren
for entry in data:
    # Durch jedes Label in dem Eintrag iterieren
    for label in entry.get('labels', []):
        category = label['category']
        # Überprüfen, ob die Kategorie in der Liste der Klassen enthalten ist
        if category in class_counts:
            # Zähler für diese Kategorie erhöhen
            class_counts[category] += 1

# Ausgabe der Anzahl von Vorkommen jeder Klasse
for category, count in class_counts.items():
    print(f"{category}: {count}")

# Anzahl der .jpg-Dateien ausgeben
print(f"Anzahl der .jpg-Dateien: {jpg_count}")