import json
import os
labels = {}

with open("FreeSurferColorLUT.txt", "r") as file:
    for line in file:
        if line.startswith("#") or line.strip() == "":
            continue  # Skip comments and empty lines

        parts = line.split()  # Split by whitespace
        if len(parts) < 2:
            continue  # Skip invalid lines
        
        label_id = int(parts[0])
        label_name = " ".join(parts[1:-4])  # Label name (excluding RGBA values)

        labels[label_id] = [tuple((int(parts[-4]), int(parts[-3]), int(parts[-2]), int(parts[-1]))),label_name]

json.dump(labels, open("labels.json", "w"), indent=4)  # Save labels to JSON file