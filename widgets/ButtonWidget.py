import pygame
from widgets.Widget import Widget


class ButtonWidget(Widget):
	def __init__(self, props:dict={}):
		super().__init__(props)

	def draw(self, screen:pygame.Surface, font:pygame.font.Font):
		super().draw(screen, font)
		x, y, w, h = self.rect.x, self.rect.y, self.rect.w, self.rect.h
		text = font.render(self.text, True, "black")
		pygame.draw.rect(screen, "darkgray", self.rect, width=2, border_radius=1)
		pygame.draw.line(screen, "white", [x, y], [x+w-1, y], 2)
		pygame.draw.line(screen, "white", [x, y], [x, y+h-1], 2)
		rect = text.get_rect(center=(self.rect.centerx, self.rect.centery))
		screen.blit(text, rect)

	def get_code_create(self, settings:dict, indent:int=0) -> str:
		ind = "\t"*indent
		return (
			f'{ind}{self.vname} = ttk.Button(self, text="{self.text}")\n'
		)
