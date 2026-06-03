import tkinter as tk
from tkinter import ttk
import tkinter.font
import consts
from Project import Project


class EventsEditorForm(ttk.Frame):

	def __init__(self, parent:ttk.Frame|tk.Tk, project:Project):
		super().__init__(parent)
		self.parent = parent
		self.widgets = project.widgets
		self.selected_widget = None
		self.selected_ev = "<Button-1>"
		self.style = ttk.Style()
		self.parent.title("Events editor")
		self.font = ["Segoe UI", 11]
		self.parent.geometry("1090x760")
		default_font = tk.font.nametofont("TkDefaultFont")
		default_font.configure(family="Segoe UI", size=11)
		self.__build_ui()
		self.__bind_events()
		self.__refresh_lbox()

	def __build_ui(self):
		#remove_btn
		self.remove_btn = ttk.Button(self, text="Remove")
		self.remove_btn.place(x=120, y=10, width=90, height=30)
		#add_btn
		self.add_btn = ttk.Button(self, text="Save")
		self.add_btn.place(x=10, y=10, width=90, height=30)
		#widget_cbox
		self.widget_cbox_var = tk.StringVar()
		self.widget_cbox = ttk.Combobox(self, font=self.font,
							textvariable=self.widget_cbox_var)
		self.widget_cbox.place(x=390, y=10, width=200, height=30)
		self.widget_cbox["values"] = [widget.name for widget in self.widgets]
		if len(self.widgets) > 0:
			self.widget_cbox.current(0)
			if self.selected_widget is None:
				self.selected_widget = self.widgets[0]
		#events_lbox
		self.events_lbox = tk.Listbox(self, font=self.font, selectmode="single")
		self.events_lbox.place(x=10, y=50, width=200, height=690)
		#text
		self.text = tk.Text(self, font=["Consolas", 11], wrap=tk.WORD)
		self.text.place(x=220, y=80, width=860, height=660)
		self.text.insert(tk.END, consts.DEFAULT_TEXT)
		#label_1
		self.label_1 = ttk.Label(self, text="Select a widget:")
		self.label_1.place(x=220, y=10, width=160, height=30)
		#label_2
		self.label_2 = ttk.Label(self, text="Select an event:")
		self.label_2.place(x=600, y=10, width=160, height=30)
		#info_label
		self.info_label = ttk.Label(self, text="")
		self.info_label.place(x=220, y=50, width=860, height=30)
		self.info_label.config(text=consts.EVENTS[self.selected_ev])
		#event_cbox
		self.event_cbox_var = tk.StringVar()
		self.event_cbox = ttk.Combobox(self, font=self.font, textvariable=self.event_cbox_var)
		self.event_cbox.place(x=770, y=10, width=200, height=30)
		self.event_cbox["values"] = list(consts.EVENTS.keys())
		self.event_cbox.current(0)
		#close_btn
		self.close_btn = ttk.Button(self, text="Close")
		self.close_btn.place(x=980, y=10, width=100, height=30)
		self.pack(fill="both", expand=True)

	def __bind_events(self):
		self.add_btn.bind("<Button-1>", self.add_btn__Button_1)
		self.close_btn.bind("<Button-1>", self.close_btn__Button_1)
		self.remove_btn.bind("<Button-1>", self.remove_btn__Button_1)
		self.event_cbox.bind("<<ComboboxSelected>>", self.event_cbox__ComboboxSelected)
		self.widget_cbox.bind("<<ComboboxSelected>>", self.widget_cbox__ComboboxSelected)
		self.events_lbox.bind("<<ListboxSelect>>", self.events_lbox__ListboxSelect)

	@staticmethod
	def run(project:Project):
		root = tk.Tk()
		form = EventsEditorForm(root, project)
		root.mainloop()
		return form

	def __refresh_lbox(self):
		if self.selected_widget is None: return
		self.events_lbox.delete(0, tk.END)
		for i, ev in enumerate(self.selected_widget.bindings):
			self.events_lbox.insert(i, ev)
		# Bindings is a dict with keys like "<Button-1>".
		# Value is a text (code) to execute.
		self.text.delete("1.0", tk.END)
		if self.selected_ev in self.selected_widget.bindings:
			self.text.insert(tk.END, self.selected_widget.bindings[self.selected_ev])
		else:
			self.text.insert(tk.END, consts.DEFAULT_TEXT)
		# If listbox contains currentyly selected event,
		# hilight that event on listbox.
		if self.selected_ev in self.selected_widget.bindings:
			idx = list(self.selected_widget.bindings.keys()).index(self.selected_ev)
			self.events_lbox.selection_set(idx)
			self.events_lbox.see(idx)

	def __save_text(self):
		self.selected_widget.bindings[self.selected_ev] = self.text.get("1.0", tk.END).strip()

	def add_btn__Button_1(self, event:tk.Event):
		if self.selected_widget is None: return
		self.__save_text()
		self.__refresh_lbox()

	def close_btn__Button_1(self, event:tk.Event):
		self.parent.after_idle(self.parent.destroy)

	def remove_btn__Button_1(self, event:tk.Event):
		selections = self.events_lbox.curselection() # A list of selected indices.
		for i in selections:
			ev = self.events_lbox.get(i)
			self.events_lbox.delete(i)
			if ev in self.selected_widget.bindings:
				del self.selected_widget.bindings[ev]

	def event_cbox__ComboboxSelected(self, event:tk.Event):
		self.selected_ev = self.event_cbox_var.get()
		self.info_label.config(text=consts.EVENTS[self.selected_ev])

	def widget_cbox__ComboboxSelected(self, event:tk.Event):
		widget_name = self.widget_cbox_var.get()
		# self.__save_text()
		for widget in self.widgets:
			if widget.name == widget_name:
				self.selected_widget = widget
				break
		self.__refresh_lbox()

	def events_lbox__ListboxSelect(self, event:tk.Event):
		selections = self.events_lbox.curselection() # A list of selected indices.
		if not selections: return
		# Load a text from the currently selected item.
		ev = self.selected_ev = self.events_lbox.get(selections[0])
		self.event_cbox.set(ev)
		self.info_label.config(text=consts.EVENTS[ev])
		self.text.delete("1.0", tk.END)
		self.text.insert(tk.END, self.selected_widget.bindings[ev])


if __name__ == "__main__":
	root = tk.Tk()
	app = EventsEditorForm(root, [])
	root.mainloop()
