import pygame

class Handles:
	def __init__(self, widget_rect:pygame.rect.Rect):
		self.size = 7
		self.widget_rect:pygame.rect.Rect = widget_rect
		self.__init_rectangles()

	def __init_rectangles(self):
		s = self.size
		x, y, w, h = self.widget_rect.x, self.widget_rect.y, self.widget_rect.w, self.widget_rect.h
		self.rectangles = [ # Clockwise order.
			pygame.rect.Rect(x-s,       y-s,       s, s), # NW
			pygame.rect.Rect(x+w/2-s/2, y-s,       s, s), # NN
			pygame.rect.Rect(x+w,       y-s,       s, s), # NE
			pygame.rect.Rect(x+w,       y+h/2-s/2, s, s), # EE
			pygame.rect.Rect(x+w,       y+h,       s, s), # SE
			pygame.rect.Rect(x+w/2-s/2, y+h,       s, s), # SS
			pygame.rect.Rect(x-s,       y+h,       s, s), # SW
			pygame.rect.Rect(x-s,       y+h/2-s/2, s, s), # WW
		]

	def set_xy(self, x:int, y:int):
		self.widget_rect.x = x
		self.widget_rect.y = y
		self.__init_rectangles()

	def set_wh(self, w:int, h:int):
		self.widget_rect.w = w
		self.widget_rect.h = h
		self.__init_rectangles()

	def draw(self, screen:pygame.Surface):
		for rect in self.rectangles:
			pygame.draw.rect(screen, "blue", rect, width=0, border_radius=0)

	def collidepoint(self, pos:tuple[int, int]) -> str:
		if not pos: return None
		d = [ 'NW', 'NN', 'NE', 'EE', 'SE', 'SS', 'SW', 'WW' ]
		for i, rect in enumerate(self.rectangles):
			if rect.collidepoint(pos):
				return d[i]
		return None


class Widget:
	def __init__(self, text:str, x:int, y:int, w:int, h:int, enabled:bool):
		self.text = text
		self.offset_x, self.offset_y = 0, 0
		self.is_enabled = enabled
		self.is_active = False
		self.drag_mode = False
		self.resize_mode = False
		self.rect = pygame.rect.Rect(x, y, w, h)
		self.handles = Handles(widget_rect=self.rect)
		self.curr_handle = False
		self.properties:dict = {
			"x": self.rect.x, "y": self.rect.y,
			"width": self.rect.w, "height": self.rect.h,
			"text": self.text, "is_enabled": self.is_enabled,
		}

	def get_properties(self) -> dict:
		self.properties.update({
			"x": self.rect.x, "y": self.rect.y,
			"width": self.rect.w, "height": self.rect.h,
			"text": self.text, "is_enabled": self.is_enabled, })
		return self.properties

	def set_properties(self, properties:dict):
		self.properties.update(properties)
		self.rect = pygame.rect.Rect(
			self.properties["x"], self.properties["y"],
			self.properties["width"], self.properties["height"] )
		self.text = self.properties["text"]
		self.is_enabled = self.properties["is_enabled"]
		self.handles = Handles(self.rect)

	def get_code(self) -> str:
		return "#TODO: add widget\n"

	def collidepoint(self, pos:tuple[int, int]) -> bool:
		return pos and self.rect.collidepoint(pos)
	
	def draw(self, screen:pygame.Surface):
		if self.is_active: # Draw the selection.
			self.handles.draw(screen)

	def handle_event(self, event:pygame.event.Event):
		pos = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN:
			self.on_mousedown(pos, event.button)			
		elif event.type == pygame.MOUSEMOTION:
			self.on_mousemove(pos)
		elif event.type == pygame.MOUSEBUTTONUP:
			self.on_mouseup(pos, event.button)

	def __check_boundary_conditions(self):
		if self.rect.x < 0: self.rect.x = 0
		if self.rect.y < 0: self.rect.y = 0
		if self.rect.w < 10: self.rect.w = 10
		if self.rect.h < 10: self.rect.h = 10

	def on_click(self, pos:tuple[int, int], button:int=1):
		if button == 3 and self.collidepoint(pos):
			self.is_active = True
			self.on_rclick()
		elif self.collidepoint(pos): # The click was performed on a widget.
			self.is_active = not self.is_active
		elif pos: # The click was performed somewhere else.
			self.is_active = False

	def on_rclick(self):
		...

	def on_mousemove(self, pos:tuple[int, int]):
		handle = self.handles.collidepoint(pos)
		if self.is_active:
			if handle in ("NW", "SE"):
				pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENWSE)
			elif handle in ("NN", "SS"):
				pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
			elif handle in ("NE", "SW"):
				pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENESW)
			elif handle in ("EE", "WW"):
				pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
			else:
				pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
		else:
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
		#
		if self.drag_mode:
			self.rect.x = pos[0] + self.offset_x
			self.rect.y = pos[1] + self.offset_y
			self.__check_boundary_conditions()
			self.handles.set_xy(self.rect.x, self.rect.y)
		if self.resize_mode:
			if self.curr_handle == "NW":
				self.rect.w = self.rect.w + self.rect.x - pos[0]
				self.rect.h = self.rect.h + self.rect.y - pos[1]
				self.rect.x = pos[0]
				self.rect.y = pos[1]
			elif self.curr_handle == "NN":
				self.rect.h = self.rect.h + self.rect.y - pos[1]
				self.rect.y = pos[1]
			elif self.curr_handle == "NE":
				self.rect.w = pos[0] - self.rect.x
				self.rect.h = self.rect.h + self.rect.y - pos[1]
				self.rect.y = pos[1]
			elif self.curr_handle == "EE":
				self.rect.w = pos[0] - self.rect.x
			elif self.curr_handle == "SE":
				self.rect.w = pos[0] - self.rect.x
				self.rect.h = pos[1] - self.rect.y
			elif self.curr_handle == "SS":
				self.rect.h = pos[1] - self.rect.y
			elif self.curr_handle == "SW":
				self.rect.w = self.rect.w + self.rect.x - pos[0]
				self.rect.h = pos[1] - self.rect.y
				self.rect.x = pos[0]
			elif self.curr_handle == "WW":
				self.rect.w = self.rect.w + self.rect.x - pos[0]
				self.rect.x = pos[0]
			self.__check_boundary_conditions()
			# Move handles to a new position.
			self.handles.set_wh(self.rect.w, self.rect.h)
		# End if

	def on_mousedown(self, pos:tuple[int, int], button:int=1):
		if button != 1:
			return
		if self.is_active and self.collidepoint(pos):
			self.drag_mode = True
			self.offset_x = self.rect.x - pos[0]
			self.offset_y = self.rect.y - pos[1]
			return
		self.curr_handle = self.handles.collidepoint(pos)
		if self.is_active and self.curr_handle:
			self.resize_mode = True
		else:
			self.curr_handle = False

	def on_mouseup(self, pos:tuple[int, int], button:int=1):
		if button != 1:
			self.on_click(pos, button)
		elif pos and self.drag_mode:
			self.drag_mode = False
		elif pos and self.resize_mode:
			self.resize_mode = False
		else:
			self.on_click(pos, button)