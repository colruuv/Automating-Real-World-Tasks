#!/usr/bin/env python3

import os
from PIL import Image

user = os.environ.get('USER')
old_path = '/home/{}/supplier-data/images/'.format(user)
#new_path = '/supplier-data/images/'

for image in os.listdir(old_path):
	if not image.startswith('.') and 'tiff' in image:
		image_path = image_directory + image_name
		path = os.path.splitext(image_path)[0]
		img = Image.open(image_path)
		new_path = '{}.jpeg'.format(path)
		img.resize((600, 400)).convert("RGB").save(new_path, "JPEG")
		img.close()