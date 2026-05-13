"""Functions for drawing in the pygame window."""

import pygame

def show_hint(screen: pygame.Surface, font: pygame.font.Font):
	"""Show hints at the bottom."""
	s = f"F1 - help  :  F2 - save  :  F3 - load  :  F4 - settings"
	text = font.render(s, False, [0, 0, 0])
	screen.blit(text, [5, screen.get_size()[1]-25])

def draw_grid(screen: pygame.Surface, size: int):
	"""Draws a grid (dots) in the background."""
	gs = size
	if gs < 2: return
	x, y = gs, gs
	while x < screen.get_width():
		while y < screen.get_height():
			screen.set_at([x, y], "black")
			y += gs
		x += gs
		y = gs
