import pygame
from widgets.Widget import Widget


class ComboboxWidget(Widget):
	def __init__(self, props:dict={}):
		super().__init__(props)
		self.values = props.get("values", [self.text])

	def draw(self, screen:pygame.Surface, font:pygame.font.Font):
		super().draw(screen)
		x, y, w, h = self.rect.x, self.rect.y, self.rect.w, self.rect.h
		old_clip = screen.get_clip()
		screen.set_clip(self.rect)

		# Background
		pygame.draw.rect(screen, "white", self.rect, width=0, border_radius=1)

		# Text
		text = font.render(self.text, True, "black")
		screen.blit(text, [x+2, y])

		# Down arrow
		rect = pygame.rect.Rect(x+w-20, y, 20, h)
		pygame.draw.rect(screen, "white", rect, width=0, border_radius=1)
		rect.x += 2		
		pygame.draw.line(screen, "dimgray", [rect.x   , rect.y + rect.h/2-3],
				   							 [rect.x+6 , rect.y + rect.h/2+3], 2)		
		pygame.draw.line(screen, "dimgray", [rect.x+6 , rect.y + rect.h/2+3],
				   							 [rect.x+12, rect.y + rect.h/2-3], 2)
		
		# Border
		pygame.draw.rect(screen, "dimgray", self.rect, width=1, border_radius=1)
		screen.set_clip(old_clip)

	def get_code_create(self, settings:dict, indent:int=0):
		ind = "\t"*indent
		return (
			f'{ind}{self.variable} = tk.StringVar()\n'
			f'{ind}{self.vname} = ttk.Combobox(self, font=self.font, textvariable={self.variable})\n'
			f'{ind}{self.vname}["values"] = ["{",".join(self.values)}"]\n'
			f'{ind}{self.vname}.current(0)\n'
		)
