import pygame
from widgets.Widget import Widget


class ListboxWidget(Widget):
	def __init__(self, props:dict={}):
		super().__init__(props)
		self.values = props.get("values", [self.text])

	def draw(self, screen:pygame.Surface, font:pygame.font.Font):
		super().draw(screen)
		old_clip = screen.get_clip()
		screen.set_clip(self.rect)
		x, y = self.rect.x, self.rect.y
		text = font.render(self.text, True, "black")
		pygame.draw.rect(screen, "white", self.rect, width=0, border_radius=1)
		pygame.draw.rect(screen, "dimgray", self.rect, width=1, border_radius=1)
		screen.blit(text, [x+2, y])
		screen.set_clip(old_clip)

	def get_code_create(self, settings:dict, indent:int=0):
		ind = "\t"*indent
		return (
			f'{ind}{self.vname} = tk.Listbox(self, font=self.font)\n'
			f'{ind}{self.vname}.insert(1, "{self.values[0]}")\n'
		)
