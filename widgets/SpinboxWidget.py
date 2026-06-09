import pygame
from widgets.Widget import Widget


class SpinboxWidget(Widget):
	def __init__(self, props:dict={}):
		super().__init__(props)

	def draw(self, screen:pygame.Surface, font:pygame.font.Font):
		super().draw(screen)
		old_clip = screen.get_clip()
		screen.set_clip(self.rect)
		x, y, w, h = self.rect.x, self.rect.y, self.rect.w, self.rect.h
		text = font.render(self.text, True, "black")
		pygame.draw.rect(screen, "white", self.rect, width=0, border_radius=1)

		# Draw two boxes with arrows on the right side
		a = h/2 # a side of the square
		X = x + w - a # calculate X coord for the boxes
		mx, my = X + a/2, y + a/2 # get the center of the upper box
		rect1 = pygame.rect.Rect(X, y,   a, a)
		rect2 = pygame.rect.Rect(X, y+a, a, a)
		
		# Draw filling.
		pygame.draw.rect(screen, "whitesmoke", rect1, width=0, border_radius=1)
		pygame.draw.rect(screen, "whitesmoke", rect2, width=0, border_radius=1)
		# Draw borders.
		pygame.draw.rect(screen, "gray", rect1, width=1, border_radius=1)
		pygame.draw.rect(screen, "gray", rect2, width=1, border_radius=1)

		# Draw first arrow
		points = [ (mx-3, my+2), (mx, my-2), (mx+3, my+2) ]
		pygame.draw.polygon(screen, "black", points)

		# Draw second arrow
		my = y + 1.5*a # go to the bottom box
		points = [ (mx-3, my-2), (mx, my+2), (mx+3, my-2) ]
		pygame.draw.polygon(screen, "black", points)
	
		# Draw the main border and place a text.
		pygame.draw.rect(screen, "dimgray", self.rect, width=1, border_radius=1)
		screen.blit(text, [x+2, y])
		screen.set_clip(old_clip)

	def get_code_create(self, settings:dict, indent:int=0):
		ind = "\t"*indent
		return (
			f'{ind}{self.vname} = tk.Spinbox(self, font=self.font)\n'
			f'{ind}{self.vname}.config(state="normal")\n'
		)
