import pygame
from widgets.Widget import Widget


class EntryWidget(Widget):
	def __init__(self, props:dict={}):
		super().__init__(props)

	def draw(self, screen:pygame.Surface, font:pygame.font.Font):
		super().draw(screen)
		old_clip = screen.get_clip()
		screen.set_clip(self.rect)
		x, y, w, h = self.rect.x, self.rect.y, self.rect.w, self.rect.h
		text = font.render(self.text, True, "black")
		pygame.draw.rect(screen, "white", self.rect, width=0, border_radius=1)
		pygame.draw.rect(screen, "dimgray", self.rect, width=1, border_radius=1)
		rect = text.get_rect(center=(self.rect.centerx, self.rect.centery))		
		screen.blit(text, [x+2, y])
		screen.set_clip(old_clip)

	def get_code_create(self, settings:dict, indent:int=0):
		ind = "\t"*indent
		return (
			f'{ind}{self.variable} = tk.StringVar()\n'
			f'{ind}{self.vname} = ttk.Entry(self, font=self.font, '
			f'textvariable={self.variable})\n'
			f'{ind}{self.vname}.insert(0, "{self.text}")\n'
		)
