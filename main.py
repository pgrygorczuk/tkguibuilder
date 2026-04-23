from forms.WidgetSelectForm import WidgetSelectForm
from forms.PropsEditorForm import PropsEditorForm
from widgets.ButtonWidget import ButtonWidget
from widgets.LabelWidget import LabelWidget
from CodeGenerator import CodeGenerator
from common import *
import pygame

pygame.init()
screen = pygame.display.set_mode(get_settings("form.size"))
font = pygame.font.Font(get_settings("font.family"), get_settings("font.size"))
pygame.display.set_caption(get_settings("form.title"))
clock = pygame.time.Clock()
running = True

widgets = load_pic(get_workspace_path("widgets.pic"))

def save():
	codegen = CodeGenerator()
	code = codegen.generate_code(widgets)
	save_text(code, get_workspace_path("main.py"))
	save_pic(widgets, get_workspace_path("widgets.pic"))

def on_rclick(widget=None):
	if widget:
		props = widget.get_properties()
		PropsEditorForm("Edit properties", props).mainloop()
		widget.set_properties(props=props)
	else:
		pos = pygame.mouse.get_pos()
		props = { "widget": None, "x": pos[0], "y": pos[1] }
		WidgetSelectForm("Widget select", props).mainloop()
		# Add selected widget.
		if props["widget"] == "Label":
			widgets.append(LabelWidget(props))
		elif props["widget"] == "Button":
			widgets.append(ButtonWidget(props))


while running:
	pos = pygame.mouse.get_pos()
	clicked_widget = None
	# Loop through events.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		# Loop through widgets to handle an event.
		for widget in widgets:
			widget.handle_event(event)
			if widget.collidepoint(pos):
				clicked_widget = widget
		# Right mouse click (button 3).
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
			on_rclick(clicked_widget) # Right mouse button has been clicked.
		# Keys
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_F1:
				...
			elif event.key == pygame.K_F2:
				save()

	# Draw widgets
	screen.fill("whitesmoke")
	for widget in widgets:
		widget.draw(screen)

	pygame.display.flip() # Update the display.
	# It will compute how many milliseconds have passed since the previous call.
	dt = clock.tick(10)

pygame.quit()
