import pygame, time
from widgets.Widget import Widget
import actions, draw, utils
from Project import Project

pygame.init()
project = Project().load() # Create a new project.
# Configure the pygame window.
pygame.display.set_caption(project.get_settings("form.title"))
screen = pygame.display.set_mode(project.get_settings("form.size"),
								 pygame.RESIZABLE)
font = pygame.font.Font("fonts/"+project.get_settings("font.family"),
						utils.pt2px(project.get_settings("font.size")))
clock = pygame.time.Clock()
click_time = 0		# To detect a double click.
running = True		# It's true as long as the program is running.
hint_visible = True # To show a hint or not.


while running:
	# Main loop.
	pos = pygame.mouse.get_pos()
	clicked_widget:Widget|None = None
	active_widget:Widget|None = None
	
	# Loop through events.
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

		# Loop through widgets to handle an event.
		for widget in project.widgets:
			widget.handle_event(event)
			if widget.collidepoint(pos):
				clicked_widget = widget
			if widget.is_active:
				active_widget = widget

		# Right mouse click (button 3).
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
			if clicked_widget:
				actions.widget_context_menu(clicked_widget)
			else:
				actions.context_menu(coords=pos, project=project)

		# Double mouse click (button 1).
		elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			if active_widget and time.time() - click_time < 0.4: # Detect double click.
				actions.widget_context_menu(active_widget)
			click_time = time.time()

		# Handle key events.
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_F1:
				...
			elif event.key == pygame.K_F2:
				actions.save(project)
			elif event.key == pygame.K_DELETE and active_widget:
				project.remove_widget(active_widget)

	# Draw widgets.
	screen.fill("whitesmoke")
	draw.draw_grid(screen, Widget.grid_size)
	for widget in project.widgets:
		widget.draw(screen, font)
	if hint_visible:
		draw.show_hint(screen, font)

	# Update the display.
	pygame.display.flip()
	# It will compute how many milliseconds have passed since the previous call.
	dt = clock.tick(10)

pygame.quit()
