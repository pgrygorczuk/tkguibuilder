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

	def get_code(self):
		code = super().get_code()
		code += f'{self.name} = ttk.Label(root, text="{self.text}")\n'
		code += f'{self.name}.place(x={self.rect.x}, y={self.rect.y}, '
		code += f'width={self.rect.width}, height={self.rect.height})\n'
		return code
	