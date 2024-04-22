# Convert label (.txt) files, so that labels match with BDD100K dataset

import os

# Verzeichnis mit den Textdateien
directory = '/home/krones2/Schreibtisch/Yolo/LicensePlate/val/labels/'

# Durchlaufen aller Textdateien im Verzeichnis
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            # Lese den Inhalt der Textdatei
            lines = file.readlines()
        with open(filepath, 'w') as file:
            # Durchlaufen aller Zeilen und Ändern der Klassennummern
            for line in lines:
                # Teile die Zeile anhand von Leerzeichen auf
                parts = line.split()
                # Ersetze die Klasse 0 durch 7 und Klasse 1 durch 2
                if parts[0] == '0':
                    parts[0] = '7'
                elif parts[0] == '1':
                    parts[0] = '2'
                # Schreibe die geänderte Zeile in die Datei
                file.write(' '.join(parts) + '\n')
