"""A set of constant (read only) values."""

DEFAULT_TEXT = (
    "widget, parent = event.widget, event.widget.master\n"
	"" )

EVENTS_COMMON = {
	"<Button-1>"  : "Left mouse button",
	"<Button-2>"  : "Middle mouse button",
	"<Button-3>"  : "Right mouse button",
	"<Button-4>"  : "Scroll up",
	"<Button-5>"  : "Scroll down",
	"<Motion>"    : "Mouse move",
	"<B1-Motion>" : "Mouse move with the LMB pressed",
}

EVENTS = {
	"Treeview": {
		"<<TreeviewSelect>>" : "Select an item from the Treeview widget",
		"<<TreeviewOpen>>" 	 : "Open an item from the Treeview widget",
		"<<TreeviewClose>>"  : "Close an item from the Treeview widget",
	},
	"Combobox": {
		"<<ComboboxSelected>>" : "Select items from the Combobox widget",
	},
	"Listbox": {
		"<<ListboxSelect>>" : "Select items from the Listbox widget"
	},
}

HELP = """\
...
"""

def get_events(class_name):
	if class_name in EVENTS:
		return EVENTS_COMMON | EVENTS[class_name]
	return EVENTS_COMMON

def get_event_desc(event_name):
	if event_name in EVENTS_COMMON:
		return EVENTS_COMMON[event_name]
	for class_name in EVENTS:
		if event_name in EVENTS[class_name]:
			return EVENTS[class_name][event_name]
	return ""
