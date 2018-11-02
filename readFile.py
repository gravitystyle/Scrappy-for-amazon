import json

with open('categories.list') as file:
	data = json.load(file)
	print(data)