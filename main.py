import pygame
from forms.WidgetSelectForm import WidgetSelectForm
from widgets.LabelWidget import LabelWidget
from widgets.ButtonWidget import ButtonWidget
from common import *

pygame.init()
screen = pygame.display.set_mode(get_settings("form.size"))
font = pygame.font.Font(get_settings("font.family"), get_settings("font.size"))
pygame.display.set_caption(get_settings("form.title"))
clock = pygame.time.Clock()
running = True

widgets = [
	ButtonWidget("Button", 100, 100, 100, 25, True),
]

def on_rclick():
	pos = pygame.mouse.get_pos()
	props = { "widget": None }
	WidgetSelectForm("Widget select", props).mainloop()
	# Add selected widget.
	if props["widget"] == "Label":
		widgets.append(LabelWidget("Label", pos[0], pos[1], 100, 25, True))
	elif props["widget"] == "Button":
		widgets.append(ButtonWidget("Button", pos[0], pos[1], 100, 25, True))


while running:
	# Loop through events.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
			on_rclick() # Right mouse button has been clicked.	
		# Loop through widgets to handle an event.
		for widget in widgets:
			widget.handle_event(event)

	# Draw widgets
	screen.fill("whitesmoke")
	for widget in widgets:
		widget.draw(screen)

	pygame.display.flip() # Update the display.
	# It will compute how many milliseconds have passed since the previous call.
	dt = clock.tick(10)

pygame.quit()
