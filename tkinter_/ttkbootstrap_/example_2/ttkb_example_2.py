import tkinter as tk

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")
root.geometry("800x600")
root.configure(padx=10, pady=10)
root.place_window_center()

assembly_frame = ttk.LabelFrame(
    root, text="Assemblies:", bootstyle=(SECONDARY,), padding=(7, 7, 7, 7)
)
assembly_frame.grid(column=0, row=0, sticky=(N, S, W))

assemblies = [f"Assembly {i}" for i in range(1, 41)]
assembly_var = tk.StringVar(value=assemblies)
assembly_list_box = tk.Listbox(assembly_frame, listvariable=assembly_var)
assembly_list_box.pack(side=LEFT)

root.mainloop()
