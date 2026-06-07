import pygame
from widgets.Widget import Widget


class LabelWidget(Widget):
	def __init__(self, props:dict={}):
		super().__init__(props)

	def draw(self, screen:pygame.Surface, font:pygame.font.Font):
		super().draw(screen)
		text = font.render(self.text, True, "black")
		pygame.draw.rect(screen, "lightgray", self.rect, width=1, border_radius=1)
		rect = text.get_rect(center=(self.rect.centerx, self.rect.centery))
		screen.blit(text, rect)

	def get_code_create(self, settings:dict, indent:int=0):
		ind = "\t"*indent
		return (
			f'{ind}{self.vname} = ttk.Label(self, text="{self.text}")\n'
		)
