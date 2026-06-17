"""Functions generating the source code of the Tkinter application.
Appropriate templates are used here."""

from __future__ import annotations
from typing import TYPE_CHECKING
from widgets.Widget import Widget
import utils

if TYPE_CHECKING:
	from Project import Project


def get_imports(path:str, templ:str, class_name:str) -> str:
	"""Combines imports from template with custom ones."""
	code = utils.load_text(path)
	templ_imports = []
	imports = []

	def parse(lines):
		result = []
		for line in lines:
			line = line.strip()
			if (line.startswith("import") or line.startswith("from")) and \
				not line in templ_imports:
				result.append(line.replace("{class_name}", class_name))
			if line.startswith("#") or line.startswith("class"):
				break
		return result

	templ_imports = parse(templ.split("\n"))
	imports = parse(code.split("\n"))
	return "\n".join(imports)


def get_methods(path:str, class_name:str) -> str:
	"""Reads custom methods to add them again after code generation."""
	code = utils.load_text(path)
	start_reading = False
	result = ""

	for line in code.split("\n"):
		line = line.rstrip()
		ls = line.lstrip()
		if "Custom methods" in line:
			start_reading = True
			continue
		if not start_reading:
			continue
		if ls.startswith('if __name__ == "__main__":'):
			break
		result += line + "\n"

	return result.strip()


def get_post_init(path:str) -> str:
	"""Reads custom instructions from post_init function 
	to add them again after code generation."""
	code = utils.load_text(path)
	start_reading = False
	result = ""

	for line in code.split("\n"):
		line = line.rstrip()
		ls = line.lstrip()
		if "Custom init instructions" in line:
			start_reading = True
			continue
		if not start_reading:
			continue
		if ls.startswith("@"):
			break
		result += line + "\n"

	if not result or result.strip() == "...":
		return "..."
	return result.strip()


def build_callbacks(project:Project, out:str) -> None:
	"""Renders callbacks functions."""
	templ = utils.load_text("templates/callbacks.tpl")
	cb = ""
	for widget in project.widgets:
		if not widget.bindings:
			continue
		cb += f"# {widget.name}\n\n"
		cb += widget.get_callbacks()
	code = templ.format(
		callbacks = cb )
	path = project.get_workspace_path(out)
	utils.save_text(code, path)


def build(project:Project, out:str) -> None:
	"""Main function that creates resulting source code.
	Overwrites previously generated code."""
	templ = utils.load_text("templates/template0.tpl")
	path  = project.get_workspace_path(out, make_dirs=True)
	title = project.get_settings("form.title")
	size  = project.get_settings("form.size")
	font_family = project.get_settings("font.family")
	font_size   = project.get_settings("font.size")
	font_style  = project.get_settings("font.style")
	class_name  = project.get_settings("form.class_name")
	custom_imports = get_imports(path, templ, class_name)
	custom_methods = get_methods(path, class_name)
	post_init	   = get_post_init(path)
	widget:Widget
	ws = be = ""
	for widget in project.widgets:
		ws += widget.get_code(project.settings, indent=2)
		be += widget.get_bind_events(indent = 2)
	if not be:
		be = "..."
	# We use a template to generate the code.
	code = templ.format(
		title		= title,
		size		= size,
		widgets 	= ws.strip(),
		font_family = font_family,
		font_size   = font_size,
		font_style  = font_style,
		bind_events = be.strip(),
		custom_imports = custom_imports,
		custom_methods = custom_methods,
		post_init	= post_init,
		class_name	= class_name )
	utils.save_text(code, path)
