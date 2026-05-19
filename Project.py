from functools import reduce
from pathlib import Path
from widgets.Widget import Widget
from Dict import Dict
import os
import build, factory, utils

class Project:
	"""Represents the state of the entire project."""

	# Default (global) settings.
	settings:Dict = Dict.from_json("settings.json")

	def __init__(self, name:str="New project"):
		"""The project consists of menu, settings and widgets.
		The Workspace is a directory where the project is stored."""
		self.name = name
		self.menu:Dict = Dict()
		self.settings:Dict = Project.settings.copy()
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
			self.settings = Dict.from_json(workspace + "settings.json")
		if os.path.exists(workspace + "menu.json"):
			self.menu	  = Dict.from_json(workspace + "menu.json")
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
		build.build(self, "main.py")

	def get_settings(self, path:str, default:int|str|None=None):
		"""Reads a value from settings at a given path. The path should
		be composed of words separated by dots (e.g: key1.key2.key3).
		If the value is missing, a default value may be returned."""
		try:
			return self.settings.get_by_path(path)
		except KeyError as e:
			return Project.settings.get_by_path(path, default)

	@staticmethod
	def get_workspace_path(path:str="", make_dirs:bool=False) -> str:
		"""Returns a path to the current workspace or to a file
		inside it."""
		workspace = Project.settings.get_by_path("workspace")
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
		Project.settings.set_by_path("workspace", workspace)
		utils.save_json(Project.settings, "settings.json")
