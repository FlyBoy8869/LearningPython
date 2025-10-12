import tkinter as tk
import ttkbootstrap as ttk

root = ttk.Window(themename="darkly")
root.title("Menubutton Example")
root.geometry("300x300")

# Create a Menu
menu_frame = ttk.Frame(root)
menu_frame.grid(column=0, row=0, sticky="nsew")

file_menu = tk.Menu(menu_frame, tearoff=0)
file_menu.add_command(label="Option 1", command=lambda: print("Option 1 selected"))
file_menu.add_command(label="Option 2", command=lambda: print("Option 2 selected"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

option_menu = tk.Menu(menu_frame, tearoff=0)
option_menu.add_command(label="Option 1", command=lambda: print("Option 1 selected"))
option_menu.add_command(label="Option 2", command=lambda: print("Option 2 selected"))

# Create a Menubutton and associate it with the Menu
# noinspection PyArgumentList
file_menubutton = ttk.Menubutton(
    menu_frame, text="File", bootstyle="secondary", menu=file_menu
)
file_menubutton.pack(side="left", anchor="nw")

# noinspection PyArgumentList
option_menubutton = ttk.Menubutton(
    menu_frame, text="Options", bootstyle="secondary", menu=option_menu
)
option_menubutton.pack(side="left", anchor="nw")

assembly_frame = ttk.LabelFrame(root, text="Assembly", padding=(1, 4, 1, 1))
assembly_frame.grid(column=0, row=1, sticky="nsew")

assemblies = [f"Assembly {i}" for i in range(1, 41)]
assembly_var = tk.StringVar(value=assemblies)
assembly_listbox = tk.Listbox(
    assembly_frame, listvariable=assembly_var, width=20, height=0
)
assembly_listbox.pack(side="left", anchor="nw", expand=True)

root.place_window_center()
root.mainloop()
