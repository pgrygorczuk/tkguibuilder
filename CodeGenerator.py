import os
from pathlib import Path
from widgets.Widget import Widget
from widgets.LabelWidget import LabelWidget
from widgets.ButtonWidget import ButtonWidget
from common import get_settings


class CodeGenerator:
	def __init__(self):
		...
	
	def load_template(self, path:str=""):
		with open(path, "r", encoding="utf8") as f:
			return f.read()

	def save_as(self, text:str, path:str):
		if not path.startswith("app/"):
			path = "app/" + path
		directory = os.path.dirname(path)
		Path(directory).mkdir(parents=True, exist_ok=True)
		with open(path, "w+") as f:
			f.write(text)

	def generate_code(self, widgets:list[Widget]):
		templ = self.load_template("templates/template0.tpl")
		title = get_settings("form.title")
		size  = get_settings("form.size")
		ws = ""
		for widget in widgets:
			ws += widget.get_code()
		code = templ.format(
			title=title,
			size=size,
			widgets=ws )
		return code


if __name__ == "__main__":
	widgets = [
		ButtonWidget({
			"name": "button1", "text": "Button",
			"x": 100, "y": 100, "w": 100, "h": 25 }),
		LabelWidget({
			"name": "label1", "text": "Label",
			"x": 100, "y": 250, "w": 100, "h": 25 }), ]
	codegen = CodeGenerator()
	code = codegen.generate_code(widgets)
	#print(code)
	codegen.save_as(code, "main.py")

