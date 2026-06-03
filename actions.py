"""Actions triggered in response to program window events."""

import pygame
from forms.EventsEditorForm import EventsEditorForm
from forms.WidgetSelectForm import WidgetSelectForm
from forms.PropsEditorForm import PropsEditorForm
from forms.SaveForm import SaveForm
from widgets.Widget import Widget
from Project import Project
import factory, utils

def on_window_resize(screen: pygame.Surface, project: Project) -> pygame.Surface:
	w, h = screen.get_size()
	gs = Widget.grid_size
	if gs > 1:
		w = round(w / gs) * gs
		h = round(h / gs) * gs
	w, h = max(160, w), max(80, h)
	project.settings.set_by_path("form.size", [w, h])
	return pygame.display.set_mode([w, h], pygame.RESIZABLE)

def events_editor(screen: pygame.Surface, project: Project):
	form = EventsEditorForm.run(project)
	print("ev")

def save(project: Project):
	"""Builds and saves a project."""
	form = SaveForm.run("Save as", project)
	if form.action == "save":
		project.set_workspace(form.workspace_path)
		project.build()
		project.save()

def widget_context_menu(widget: Widget):
	"""Handles RMB or double click on widget. Displays properties editor."""
	props = widget.get_properties()
	PropsEditorForm("Edit properties", props).mainloop()
	widget.set_properties(props=props)

def context_menu(coords: tuple[int, int], project: Project):
	"""Default context menu displayed when clicking anywhere."""
	props = { "widget": None, "x": coords[0], "y": coords[1] }
	WidgetSelectForm("Widget select", props).mainloop()
	# Add selected widget.
	if props["widget"] is not None:
		project.widgets.append(factory.create_widget(
			widget_type = props["widget"],
			props = props))
