from typing import TypeVar
import json, os, pickle

T = TypeVar("T")

def load_json(path:str) -> dict:
	d = {}
	with open(path) as f:
		d = json.load(f)
	return d

def save_json(data:dict, path:str) -> None:
	with open(path, "w") as f:
		json.dump(data, f, indent=4)

def load_text(path:str="") -> str:
	if not os.path.exists(path):
		return ""
	with open(path, "r", encoding="utf8") as f:
		return f.read()

def save_text(text:str, path:str, overwrite:bool=True) -> None:
	if not overwrite and os.path.exists(path):
		return
	with open(path, "w+", encoding="utf8") as f:
		f.write(text)

def load_pic(path:str, default:T=[]) -> T:
	items = default
	if os.path.exists(path):
		with open(path, "rb") as f:
			items = pickle.load(f)
	return items

def save_pic(items:list|dict, path:str) -> None:
	with open(path, "wb") as f:
		pickle.dump(items, f)

# Tkinter uses points, pygame uses pixels
def pt2px(pt:int, dpi:int=96) -> int:
	return round(pt * dpi / 72)
