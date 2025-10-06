import tkinter as tk
from tkinter import ttk


def make_menu(parent):
    menubar = tk.Menu(parent)

    # ===== File Menu ===============================================================================
    file_menu = tk.Menu(menubar, background="#1C1C1C")
    file_menu.add_command(label="Exit", command=parent.destroy)
    menubar.add_cascade(label="File", menu=file_menu)
    # ===== End File Menu ===========================================================================

    return menubar
