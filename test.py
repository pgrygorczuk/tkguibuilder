import pygame, threading
import tkinter as tk
from common import *

pygame.init()
screen = pygame.display.set_mode(get_settings("form.size"))
font = pygame.font.Font(get_settings("font.family"), get_settings("font.size"))
pygame.display.set_caption(get_settings("form.title"))
clock = pygame.time.Clock()
running = True

# print(pygame.font.get_fonts())

while running:
	pos = None
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("whitesmoke")
	pygame.display.flip() # Update.
	# It will compute how many milliseconds have passed since the previous call.
	dt = clock.tick(10)

pygame.quit()
