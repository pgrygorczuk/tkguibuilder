import pygame
from widgets.Widget import Widget


class CheckbuttonWidget(Widget):
	def __init__(self, props:dict={}):
		super().__init__(props)

	def draw(self, screen:pygame.Surface, font:pygame.font.Font):
		super().draw(screen)
		old_clip = screen.get_clip()
		screen.set_clip(self.rect)
		x, y, w, h = self.rect.x, self.rect.centery - 6, 12, 12
		text = font.render(self.text, True, "black")
		pygame.draw.rect(screen, "black", pygame.Rect(x, y, w, h), width=1, border_radius=1)
		rect = text.get_rect(center=(self.rect.centerx, self.rect.centery))		
		screen.blit(text, [ x+1.5*w, y-6 ])
		screen.set_clip(old_clip)

	def get_code(self, indent:int=0):
		code = super().get_code(indent)
		ind = "\t"*indent
		return code + (
			f'{ind}{self.vname} = ttk.Checkbutton(self, text="{self.text}", takefocus=0)\n'
			f'{ind}{self.vname}.place(x={self.rect.x}, y={self.rect.y}, '
			f'width={self.rect.width}, height={self.rect.height})\n'
		)
