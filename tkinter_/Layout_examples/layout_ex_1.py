from tkinter import *

import ttkbootstrap as ttk

root = ttk.Window(themename="darkly")
root.configure(padx=5, pady=5)

content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=3, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar(value=True)
twovar = BooleanVar(value=False)
threevar = BooleanVar(value=True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay", bootstyle="secondary")
cancel = ttk.Button(content, text="Cancel", bootstyle="secondary")

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W))
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W))
one.grid(column=0, row=5)
two.grid(column=1, row=5)
three.grid(column=2, row=5)
ok.grid(column=3, row=5)
cancel.grid(column=4, row=5)

content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.place_window_center()
root.mainloop()
