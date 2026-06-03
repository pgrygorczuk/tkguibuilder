"""Functions generating the source code of the Tkinter application.
Appropriate templates are used here."""

from __future__ import annotations
from typing import TYPE_CHECKING
from widgets.Widget import Widget
from Dict import Dict
import utils

if TYPE_CHECKING:
	from Project import Project

def build_callbacks(project:Project, out:str) -> None:
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
	"""Main function that creates resulting source code."""
	templ = utils.load_text("templates/template0.tpl")
	title = project.get_settings("form.title")
	size  = project.get_settings("form.size")
	font_family = project.get_settings("font.family")
	font_size   = project.get_settings("font.size")
	font_style  = project.get_settings("font.style")
	widget:Widget
	ws = be = ""
	for widget in project.widgets:
		ws += widget.get_code(indent = 2)
		be += widget.get_bind_events(indent = 2)
	if not be:
		be = "..."
	# We use a template to generate code.
	code = templ.format(
		title		= title,
		size		= size,
		widgets 	= ws.strip(),
		font_family = font_family,
		font_size   = font_size,
		font_style  = font_style,
		bind_events = be.strip() )
	path = project.get_workspace_path(out)
	utils.save_text(code, path)
