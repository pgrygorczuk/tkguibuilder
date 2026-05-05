import tkinter as tk
from tkinter import ttk
import tkinter.font

class MainFrame(ttk.Frame):

	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.style = ttk.Style()
		self.parent.title("{title}")
		self.font = ["{font_family}", {font_size}]
		self.parent.geometry("{size[0]}x{size[1]}")
		default_font = tk.font.nametofont("TkDefaultFont")
		default_font.configure(family="{font_family}", size={font_size})
		self.__build_ui()

	def __build_ui(self):
		{widgets}
		self.pack(fill="both", expand=True)


if __name__ == "__main__":
	root = tk.Tk()
	app = MainFrame(root)
	root.mainloop()
