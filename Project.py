from functools import reduce
from pathlib import Path
from typing import Any
from widgets.Widget import Widget
import os
import build, factory, utils

class Project:
	"""Represents the state of the entire project."""

	# Default (global) settings.
	settings:dict = utils.load_json("settings.json")

	def __init__(self, name:str="New project"):
		"""The project consists of menu, settings and widgets.
		The Workspace is a directory where the project is stored."""
		self.name:str = name
		self.menu:dict = {}
		self.settings:dict = Project.settings.copy()
		self.widgets:list[Widget] = []

	def save(self):
		"""Saves current project."""
		workspace = Project.get_workspace_path(path="", make_dirs=True)
		utils.save_pic(self.widgets, workspace + "widgets.pic")
		utils.save_json(self.menu, workspace + "menu.json")
		utils.save_json(self.settings, workspace + "settings.json")

	def load(self):
		"""Loads project from files."""
		workspace = Project.get_workspace_path()
		if os.path.exists(workspace + "settings.json"):
			self.settings = utils.load_json(workspace + "settings.json")
		if os.path.exists(workspace + "menu.json"):
			self.menu	  = utils.load_json(workspace + "menu.json")
		if os.path.exists(workspace + "widgets.pic"):
			self.widgets  = utils.load_pic(workspace + "widgets.pic")
		Widget.grid_size = int(self.get_settings("grid_size", 0))
		return self

	def add_widget(self, widget_type:str, props:dict):
		"""Adds a new widget to the project."""
		self.widgets.append(
			factory.create_widget(widget_type, props) )

	def remove_widget(self, widget:Widget):
		"""Removes a widget."""
		self.widgets.remove(widget)

	def build(self):
		"""Generates a source code."""
		class_name = self.get_settings("form.class_name")
		build.build(self, class_name+".py")
		build.build_callbacks(self, class_name+"_callbacks.py")

	def get_settings(self, path:str, default:Any=None) -> Any:
		"""Reads a value from settings at a given path. The path should
		be composed of words separated by dots (e.g: key1.key2.key3).
		If the value is missing, a default value may be returned."""
		keys = path.split(".")
		def get_val(d, default=None, i=0) -> Any:
			value = d.get(keys[i], default)
			if type(value) == dict and len(keys) > i+1:
				return get_val(value, default, i+1)
			return value
		# Try to get local settings.
		v = get_val(self.settings)
		if v is None: # Get global settings.
			return get_val(Project.settings, default)
		return v

	@staticmethod
	def get_workspace_path(path:str="", make_dirs:bool=False) -> str:
		"""Returns a path to the current workspace or to a file
		inside it."""
		workspace = Project.settings["workspace"]
		if not path.startswith(workspace):
			path = workspace + path
		if make_dirs:
			directory = os.path.dirname(workspace)
			Path(directory).mkdir(parents=True, exist_ok=True)
		return path
	
	@staticmethod
	def set_workspace(workspace:str) -> None:
		"""Updates a workspace."""
		if not workspace.endswith("/"): workspace += "/"
		Project.settings["workspace"] = workspace
		utils.save_json(Project.settings, "settings.json")
