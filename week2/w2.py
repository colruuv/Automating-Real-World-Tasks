#!/usr/bin/env python3

import os
import requests
import json

path = "/data/feedback/"
keys = ["title", "name", "date", "feedback"]
URL_ENDPOINT = "http://34.66.73.23/feedback/"
feedbacks = []

folder = os.listdir(path)

for file in folder:
	keycount = 0
	fb = {}
	with open(path + file) as fl:
		for line in fl:
			value = line.strip()
			fb[keys[keycount]] = value
			keycount += 1
		feedbacks.append(fb)
	response = requests.post(URL_ENDPOINT, json=fb)

print(response.request.body)
print(response.status_code)