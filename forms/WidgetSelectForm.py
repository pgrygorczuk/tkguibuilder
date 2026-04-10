import tkinter as tk
from tkinter import ttk


class WidgetSelectForm(tk.Tk):    
    def __init__(self, title:str="Widget selection", props:dict={}):
        super().__init__()
        self.title(title)
        self.props = props
        self.geometry("300x250")
        self.__build_ui()

    def __build_ui(self):
        main_frame = ttk.Frame(self, padding=10)
        main_frame.pack(fill="both", expand=True)

        # Configure columns
        main_frame.columnconfigure(0, weight=3)
        main_frame.columnconfigure(1, weight=1)

        widgets = [
            ("Label", self.create_label_preview),
            ("Button", self.create_button_preview),
            ("Entry", self.create_entry_preview),
            ("Combobox", self.create_combobox_preview),
            ("Checkbutton", self.create_checkbutton_preview),
        ]

        for row, (name, preview_func) in enumerate(widgets):
            # Left side (widget visualization)
            preview_frame = ttk.Frame(main_frame)
            preview_frame.grid(row=row, column=0, sticky="w", padx=5, pady=5)
            preview_func(preview_frame)

            # Right side (Add button)
            btn = ttk.Button(
                main_frame,
                text="Add",
                command=lambda n=name: self.add_widget(n)
            )
            btn.grid(row=row, column=1, padx=5, pady=5, sticky="e")

    # --- PREVIEW FUNCTIONS ---
    def create_label_preview(self, parent):
        ttk.Label(parent, text="Label").pack(anchor="w")

    def create_button_preview(self, parent):
        ttk.Button(parent, text="Button").pack(anchor="w")

    def create_entry_preview(self, parent):
        entry = ttk.Entry(parent)
        entry.insert(0, "Entry")
        entry.pack(anchor="w")

    def create_combobox_preview(self, parent):
        combo = ttk.Combobox(parent, values=["Combobox"])
        combo.set("Combobox")
        combo.pack(anchor="w")

    def create_checkbutton_preview(self, parent):
        ttk.Checkbutton(parent, text="Checkbutton").pack(anchor="w")

    # Action
    def add_widget(self, widget_name):
        # print(f"Selected widget: {widget_name}")
        self.props["widget"] = widget_name
        self.destroy()
        


if __name__ == "__main__":
    app = WidgetSelectForm()
    app.mainloop()
    