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

	def get_code(self, indent:int=0):
		code = super().get_code(indent)
		ind = "\t"*indent
		return code + (
			f'{ind}{self.variable} = tk.StringVar()\n'
			f'{ind}{self.vname} = ttk.Entry(self, font=self.font, textvariable={self.variable})\n'
			f'{ind}{self.vname}.place(x={self.rect.x}, y={self.rect.y}, '
			f'width={self.rect.width}, height={self.rect.height})\n'
			f'{ind}{self.vname}.insert(0, "{self.text}")\n'
		)
