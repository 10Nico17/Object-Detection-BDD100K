## Check frequency of the classes in the dataset

import os

# Ordnerpfad mit den Textdateien
folder_path = 'labels_to_yolo'

# Klasseninformationen
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

# Initialisiere ein Wörterbuch zum Zählen der Häufigkeit jedes Labels
label_counts = {class_name: 0 for class_name in class_names.values()}


number_files = 0
# Durchlaufe alle Textdateien im Ordner
for filename in os.listdir(folder_path):
    number_files+=1
    if filename.endswith('.txt'):
        filepath = os.path.join(folder_path, filename)
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.split()
                class_id = int(data[0])
                if class_id in class_names:
                    class_name = class_names[class_id]
                    label_counts[class_name] += 1

# Gib die Anzahl jedes Labels aus
for class_name, count in label_counts.items():
    print(f'{class_name}: {count}')


    import os

# Initialisiere ein Wörterbuch zum Zählen der Häufigkeit jeder Klassennummer
class_counts = {}

# Durchlaufe alle Textdateien im Ordner
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        filepath = os.path.join(folder_path, filename)
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                class_id = int(line.split()[0])
                class_counts[class_id] = class_counts.get(class_id, 0) + 1

# Gib die Anzahl jeder Klassennummer aus
for class_id, count in class_counts.items():
    print(f'Class {class_id}: {count}')

print('number_files: ', number_files)