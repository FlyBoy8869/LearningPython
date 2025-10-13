import tkinter as tk
import ttkbootstrap as ttk

from mainwindow import MainWindow

APP_TITLE = "CopyDocs"
WINDOW_X_DIMENSION = 800
WINDOW_Y_DIMENSION = 500

# root = tk.Tk()
root = ttk.Window(themename="darkly", minsize=(WINDOW_X_DIMENSION, WINDOW_Y_DIMENSION))
root.title(f"{APP_TITLE}")
root.geometry(f"{WINDOW_X_DIMENSION}x{WINDOW_Y_DIMENSION}")
root.configure(padx=5, pady=5)
root.update_idletasks()

# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# x = (screen_width // 2) - (WINDOW_X_DIMENSION // 2)
# y = (screen_height // 2) - (WINDOW_Y_DIMENSION // 2)
# root.geometry(f"{WINDOW_X_DIMENSION}x{WINDOW_Y_DIMENSION}+{x}+{y - (int(y * .5))}")

root.option_add("*tearOff", tk.FALSE)

MainWindow(root)

root.place_window_center()
root.mainloop()
