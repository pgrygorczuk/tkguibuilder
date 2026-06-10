import tkinter as tk
from tkinter import ttk
import tkinter.font


class WidgetSelectForm(tk.Tk):
	def __init__(self, title:str="Widget selection", props:dict={}):
		super().__init__()
		self.title(title)
		self.props = props
		self.geometry("380x640")
		self.font = ["Segoe UI", 11]
		default_font = tk.font.nametofont("TkDefaultFont")
		default_font.configure(family="Segoe UI", size=11)
		self.__build_ui()

	def __build_ui(self):
		self.grid_columnconfigure(0, weight=2)
		self.grid_columnconfigure(1, weight=1)
		ttk.Label(self, text="Choose one of the widgets you wish to add:").grid(
			row=0, columnspan=2, pady=5)

		widgets = [
			("Label"		, self.create_label_preview),
			("Button"		, self.create_button_preview),
			("Entry"		, self.create_entry_preview),
			("Combobox"		, self.create_combobox_preview),
			("Spinbox"		, self.create_spinbox_preview),
			("Checkbutton"	, self.create_checkbutton_preview),
			("Labelframe"	, self.create_labelframe_preview),
			("Listbox"		, self.create_listbox_preview),
			("Text"			, self.create_text_preview),
			("Treeview"		, self.create_treeview_preview),
		]

		for row, (name, preview_func) in enumerate(widgets):
			# Left side (widget visualization).
			preview_func().grid(row=row+1, column=0, padx=(20, 10), pady=10, sticky="ew")

			# Right side (Add button)
			btn = ttk.Button(
				self, text="Add",
				command=lambda n=name: self.add_widget(n)
			).grid(row=row+1, column=1, padx=(10, 20), pady=10, sticky="e")


	# --- PREVIEW FUNCTIONS ---
	def create_label_preview(self):
		return ttk.Label(self, text="Label")

	def create_button_preview(self):
		return ttk.Button(self, text="Button")

	def create_entry_preview(self):
		entry = ttk.Entry(self, font=self.font)
		entry.insert(0, "Entry")
		return entry

	def create_combobox_preview(self):
		combo = ttk.Combobox(self, font=self.font,
					   values=["Combobox"])
		combo.set("Combobox")
		return combo

	def create_spinbox_preview(self):
		sbox = ttk.Spinbox(self, values=["Spinbox"], font=self.font)
		sbox.set("Spinbox")
		return sbox

	def create_checkbutton_preview(self):
		return ttk.Checkbutton(self, text="Checkbutton")

	def create_labelframe_preview(self):
		lf = ttk.Labelframe(self, text="Labelframe")
		btn = ttk.Label(lf, text='...').grid(row=0, column=0)
		return lf

	def create_listbox_preview(self):
		lbox = tk.Listbox(self, width=20, height=2)
		lbox.insert(1, "Listbox")
		return lbox
		
	def create_text_preview(self):
		t = tk.Text(self, width=20, height=2, font=self.font)
		t.insert(tk.END, "Text")
		return t
	
	def create_treeview_preview(self):
		tv = ttk.Treeview(self, columns=["c1"], height=2)
		tv.column("#0", anchor="center", stretch=False, width=100)
		tv.column("#1", anchor="w", stretch=False, width=100)
		tv.heading("#0", text="C1")
		tv.heading("#1", text="C2")
		uid = tv.insert('', 'end', text='Treeview')
		return tv
		

	# Action
	def add_widget(self, widget_name):
		# print(f"Selected widget: {widget_name}")
		self.props["widget"] = widget_name
		self.destroy()
		


if __name__ == "__main__":
	app = WidgetSelectForm()
	app.mainloop()
	