"""Actions triggered in response to program window events."""

from forms.WidgetSelectForm import WidgetSelectForm
from forms.PropsEditorForm import PropsEditorForm
from forms.SaveForm import SaveForm
from widgets.Widget import Widget
from Project import Project
import factory, utils

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
	project.widgets.append(factory.create_widget(
		widget_type = props["widget"], props = props))
