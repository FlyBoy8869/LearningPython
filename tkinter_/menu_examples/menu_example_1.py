import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Menubutton Example")

# Create a Menu
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Option 1", command=lambda: print("Option 1 selected"))
menu.add_command(label="Option 2", command=lambda: print("Option 2 selected"))
menu.add_separator()
menu.add_command(label="Exit", command=root.quit)

# Create a Menubutton and associate it with the Menu
menubutton = ttk.Menubutton(root, text="File", menu=menu)
menubutton.pack(pady=10)

root.mainloop()
