import pygame
from common import *
from widgets.Widget import Widget


class LabelWidget(Widget):
	def __init__(self, props:dict={}):
		super().__init__(props)

	def draw(self, screen:pygame.Surface):
		super().draw(screen)
		font = pygame.font.Font("fonts/"+get_settings("font.family"),
						  		pt2px(get_settings("font.size")))
		text = font.render(self.text, True, "black")
		pygame.draw.rect(screen, "lightgray", self.rect, width=1, border_radius=1)
		rect = text.get_rect(center=(self.rect.centerx, self.rect.centery))
		screen.blit(text, rect)

	def get_code(self, indent:int=0):
		code = super().get_code(indent)
		ind = "\t"*indent
		return code + (
			f'{ind}{self.vname} = ttk.Label(self, text="{self.text}")\n'
			f'{ind}{self.vname}.place(x={self.rect.x}, y={self.rect.y}, '
			f'width={self.rect.width}, height={self.rect.height})\n'
		)
