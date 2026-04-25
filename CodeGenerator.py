from widgets.Widget import Widget
from widgets.LabelWidget import LabelWidget
from widgets.ButtonWidget import ButtonWidget
from common import get_settings, save_text, get_workspace_path


class CodeGenerator:
	def __init__(self):
		...

	def load_template(self, path:str) -> str:
		with open(path, "r", encoding="utf8") as f:
			return f.read()

	def generate_code(self, widgets:list[Widget]) -> str:
		templ = self.load_template("templates/template0.tpl")
		title = get_settings("form.title")
		size  = get_settings("form.size")
		font_family = get_settings("font.family")
		font_size   = get_settings("font.size")
		font_style  = get_settings("font.style")
		ws = ""
		for widget in widgets:
			ws += widget.get_code()
		code = templ.format(
			title = title,
			size = size,
			widgets = ws,
			font_family = font_family,
			font_size = font_size,
			font_style = font_style )
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
	save_text(code, get_workspace_path("main.py"))
	#print(code)

