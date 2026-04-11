import pygame
from common import *
from widgets.Widget import Widget


class LabelWidget(Widget):
	def __init__(self, text, x, y, w, h, enabled):
		super().__init__(text, x, y, w, h, enabled)

	def draw(self, screen:pygame.Surface):
		super().draw(screen)
		font = pygame.font.Font(get_settings("font.family"), get_settings("font.size"))
		text = font.render(self.text, True, "black")
		pygame.draw.rect(screen, "lightgray", self.rect, width=1, border_radius=1)
		rect = text.get_rect(center=(self.rect.centerx, self.rect.centery))
		screen.blit(text, rect)

