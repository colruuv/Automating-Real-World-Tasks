#!/usr/bin/env python3

import requests

url = 'http://35.225.185.202/upload'
user = os.environ.get('USER')
image_directory = '/home/{}/supplier-data/images/'.format(user)
files = os.listdir(image_directory)
for image in files:
	if not image.startwith('.') and 'jpeg' in image:
		image_path = image_directory + image
		with open(image_path, 'rb') as img_op:
			r = requests.post(url, files={'file': img_op})