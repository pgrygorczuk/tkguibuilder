import tkinter as tk
from tkinter import ttk
import tkinter.font
from common import *

class SaveForm(ttk.Frame):

	def __init__(self, parent:ttk.Frame, title:str):
		super().__init__(parent)
		self.parent = parent
		self.style = ttk.Style()
		self.parent.title(title)
		self.font = ["Segoe UI", 12]
		self.parent.geometry("700x140")
		default_font = tk.font.nametofont("TkDefaultFont")
		default_font.configure(family="Segoe UI", size=12)
		self.workspace_path = get_settings("workspace")
		self.action = None
		self.__build_ui()
		self.__bind_events()

	def __build_ui(self):
		#ws_label
		self.ws_label = ttk.Label(self, text="Workspace")
		self.ws_label.place(x=20, y=20, width=100, height=30)
		#ws_entry
		self.ws_entry_var = tk.StringVar()
		self.ws_entry = ttk.Entry(self, font=self.font, textvariable=self.ws_entry_var)
		self.ws_entry.place(x=130, y=20, width=500, height=30)
		self.ws_entry.insert(0, self.workspace_path)
		#cancel_btn
		self.cancel_btn = ttk.Button(self, text="Cancel")
		self.cancel_btn.place(x=530, y=80, width=100, height=30)
		#save_btn
		self.save_btn = ttk.Button(self, text="Save")
		self.save_btn.place(x=410, y=80, width=100, height=30)
		self.pack(fill="both", expand=True)

	def __bind_events(self):
		self.cancel_btn.bind("<Button-1>", self.cancel_btn__button_1)
		self.save_btn.bind("<Button-1>", self.save_btn__button_1)

	@staticmethod
	def run(title:str):
		root = tk.Tk()
		form = SaveForm(root, title)
		root.mainloop()
		return form

	def cancel_btn__button_1(self, event:tk.Event):
		self.action = None
		# self.parent.destroy()
		self.after_idle(self.parent.destroy)

	def save_btn__button_1(self, event:tk.Event):
		self.workspace_path = self.ws_entry_var.get()
		settings = load_json("settings.json")
		if settings["workspace"] != self.workspace_path:
			settings["workspace"] = self.workspace_path
			save_json(settings, "settings.json")
		self.action = "save"
		# self.parent.destroy()
		self.after_idle(self.parent.destroy)


if __name__ == "__main__":
	root = tk.Tk()
	app = SaveForm(root)
	root.mainloop()
