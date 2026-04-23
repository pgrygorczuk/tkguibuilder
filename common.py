from functools import reduce
from pathlib import Path
import json, os, pickle

settings = {}

def get_settings(path:str=""):
	global settings
	if not settings:
		settings = load_json("settings.json")
	return reduce(dict.get, path.split("."), settings)

def get_workspace_path(path:str) -> str:
	workspace = get_settings("workspace")
	if not path.startswith(workspace):
		path = workspace + path
	directory = os.path.dirname(path)
	Path(directory).mkdir(parents=True, exist_ok=True)
	return path

def load_json(path:str):
	d = {}
	with open(path) as f:
		d = json.load(f)
	return d

def save_json(data:dict, path:str):
	with open(path, "w") as f:
		json.dump(data, f)

def load_text(path:str=""):
	with open(path, "r", encoding="utf8") as f:
		return f.read()

def save_text(text:str, path:str):
	with open(path, "w+") as f:
		f.write(text)

def load_pic(path:str, default:list|dict=[]) -> list|dict:
	items = default
	if os.path.exists(path):
		with open(path, "rb") as f:
			items = pickle.load(f)
	return items

def save_pic(items:list|dict, path:str):
	with open(path, "wb") as f:
		pickle.dump(items, f)

if __name__ == "__main__":
	print(get_settings("form.size"))
