import tkinter as tk
from tkinter import ttk


class PropsEditorForm(tk.Tk):
	def __init__(self, title:str, props:dict):
		super().__init__()
		self.title(title)
		self.props = props
		self.inputs = {}
		self.__build_ui()

	def __build_ui(self):
		frame = ttk.Frame(self, padding=10)
		frame.pack(fill="both", expand=True)

		# Create inputs for each key
		for row, (key, value) in enumerate(self.props.items()):
			label = ttk.Label(frame, text=key)
			label.grid(row=row, column=0, sticky="w", padx=5, pady=5)

			if type(value) == bool:
				check_var = tk.BooleanVar(value=value)
				input = ttk.Checkbutton(frame, onvalue=1, offvalue=0, variable=check_var)
				input.grid(row=row, column=1, sticky="ew", padx=5, pady=5)
				self.inputs[key] = check_var
			else:
				input = ttk.Entry(frame)
				input.insert(0, str(value))
				input.grid(row=row, column=1, sticky="ew", padx=5, pady=5)
				self.inputs[key] = input

		# Resize Entry column
		frame.columnconfigure(1, weight=1)

		# Create buttons
		btn_frame = ttk.Frame(self)
		btn_frame.pack(fill="x", pady=10)

		close_btn = ttk.Button(btn_frame, text="Close", command=self.destroy)
		close_btn.pack(side="right", padx=5)

		save_btn = ttk.Button(btn_frame, text="Save", command=self.save)
		save_btn.pack(side="right", padx=5)

	def save(self):
		for key, entry in self.inputs.items():
			value = entry.get()

			# Try convert to int/float/bool
			if type(value) == str:
				if value.isdigit():
					value = int(value)
				else:
					try:
						value = float(value)
					except ValueError:
						if value.lower() in ("true", "false"):
							value = value.lower() == "true"

			self.props[key] = value

		print("Updated dict:", self.props)


# --- usage example ---
if __name__ == "__main__":
	props = {
		"width": 800,
		"height": 600,
		"title": "My app",
		"fullscreen": False,
		"opacity": 0.85
	}

	app = PropsEditorForm("", props)
	app.mainloop()

	print("Finally:", props)