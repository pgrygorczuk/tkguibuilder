"""Functions that create more complex objects."""

from widgets.CheckbuttonWidget import CheckbuttonWidget
from widgets.ComboboxWidget import ComboboxWidget
from widgets.ButtonWidget import ButtonWidget
from widgets.EntryWidget import EntryWidget
from widgets.LabelWidget import LabelWidget
from widgets.TextWidget import TextWidget
from widgets.Widget import Widget

def create_widget(widget_type:str, props:dict={}) -> Widget:
	"""Creates a widget object of the given type."""
	widgets = {
		"Button"	 : ButtonWidget,
		"Checkbutton": CheckbuttonWidget,
		"Combobox"	 : ComboboxWidget,
		"Entry"		 : EntryWidget,
		"Label"		 : LabelWidget,
		"Text"		 : TextWidget, }
	if widget_type in widgets:
		return widgets[widget_type](props)
	raise ValueError(f"Unknown widget type: {widget_type}")

