import pygame
from common import *
from widgets.Widget import Widget


class ButtonWidget(Widget):
	def __init__(self, text, x, y, w, h, enabled):
		super().__init__(text, x, y, w, h, enabled)

	def draw(self, screen:pygame.Surface):
		super().draw(screen)
		x, y, w, h = self.rect.x, self.rect.y, self.rect.w, self.rect.h
		font = pygame.font.Font(get_settings("font.family"), get_settings("font.size"))
		text = font.render(self.text, True, "black")
		pygame.draw.rect(screen, "darkgray", self.rect, width=2, border_radius=1)
		pygame.draw.line(screen, "white", [x, y], [x+w-1, y], 2)
		pygame.draw.line(screen, "white", [x, y], [x, y+h-1], 2)
		rect = text.get_rect(center=(self.rect.centerx, self.rect.centery))
		screen.blit(text, rect)

