import pygame
from forms.WidgetSelectForm import WidgetSelectForm
from common import *

pygame.init()
screen = pygame.display.set_mode(get_settings("form.size"))
font = pygame.font.Font(get_settings("font.family"), get_settings("font.size"))
pygame.display.set_caption(get_settings("form.title"))
clock = pygame.time.Clock()
running = True

widgets = []

def on_rclick():
	pos = pygame.mouse.get_pos()
	props = { "widget": None }
	WidgetSelectForm("Widget select", props).mainloop()
	print(f"TODO: Add {props["widget"]} at xy = {pos}.")

while running:
	pos = None
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

	pygame.display.flip() # Update.
	# It will compute how many milliseconds have passed since the previous call.
	dt = clock.tick(10)

pygame.quit()
