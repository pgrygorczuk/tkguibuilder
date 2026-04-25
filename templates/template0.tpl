import tkinter as ttk
import tkinter as tk
import tkinter.font

root = tk.Tk()
root.title("{title}")
root.minsize({size[0]}, {size[1]})
root.geometry("{size[0]}x{size[1]}+50+50")
default_font = tk.font.nametofont("TkDefaultFont")
default_font.configure(family="{font_family}", size={font_size})


# Create widgets
{widgets}


root.mainloop()