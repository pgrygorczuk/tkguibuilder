"""A set of constant (read only) values."""

DEFAULT_TEXT = (
    "widget = event.widget\n"
	"parent = widget.winfo_parent()\n"
	"" )

EVENTS = {
	"<Button-1>"  : "Left mouse button",
	"<Button-2>"  : "Middle mouse button",
	"<Button-3>"  : "Right mouse button",
	"<Button-4>"  : "Scroll up",
	"<Button-5>"  : "Scroll down",
	"<Motion>"    : "Mouse move",
	"<B1-Motion>" : "Mouse move with the LMB pressed",
}

HELP = """\
...
"""
