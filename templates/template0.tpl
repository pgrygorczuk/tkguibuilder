import tkinter as tk
from tkinter import ttk
import tkinter.font
import callbacks
{custom_imports}

class {class_name}(ttk.Frame):

	def __init__(self, parent:ttk.Frame|tk.Tk):
		"""Auto-generated method. Do not modify."""
		super().__init__(parent)
		self.parent = parent
		self.style = ttk.Style()
		self.parent.title("{title}")
		self.font = ["{font_family}", {font_size}]
		self.parent.geometry("{size[0]}x{size[1]}")
		default_font = tk.font.nametofont("TkDefaultFont")
		default_font.configure(family="{font_family}", size={font_size})
		self.__build_ui()
		self.__bind_events()
		self.__post_init()

	def __build_ui(self):
		"""Auto-generated method. Do not modify."""
		{widgets}
		self.pack(fill="both", expand=True)

	def __bind_events(self):
		"""Auto-generated method. Do not modify."""
		{bind_events}

	def __post_init(self):
		"""Custom init instructions."""
		{post_init}

	@staticmethod
	def run(data=None):
		"""Auto-generated method. Do not modify."""
		frame = MainFrame(tk.Tk())
		frame.parent.mainloop()
		return frame

	# Custom methods.
	{custom_methods}

