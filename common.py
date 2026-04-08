from functools import reduce
import json

settings = {}

def load_json(path:str):
	d = {}
	with open(path) as f:
		d = json.load(f)
	return d

def get_settings(path:str=""):
	global settings
	if not settings:
		settings = load_json("settings.json")
	return reduce(dict.get, path.split("."), settings)


if __name__ == "__main__":
	print(get_settings("form.size"))

