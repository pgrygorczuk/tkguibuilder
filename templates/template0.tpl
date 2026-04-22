import tkinter as tk
import tkinter as ttk

root = tk.Tk()
root.title("{title}")
root.minsize({size[0]}, {size[1]})
root.geometry("{size[0]}x{size[1]}+50+50")

# Create widgets
{widgets}


root.mainloop()