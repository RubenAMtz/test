import json
import os

ann = {}
file = 'DS\Labeled\Falla190.json'
f = open(f'{file}')
data = json.load(f)

for image in data['images']:
    print(image['file_name'], image['id'])
    ann[image['file_name']]=[]

    for annotation in data['annotations']:
        if annotation['image_id'] == image['id']:
            ann[image['file_name']].append(annotation.get('bbox'))
print(ann)

f.close()