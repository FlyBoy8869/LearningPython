import tkinter as tk

from mainwindow import MainWindow

APP_TITLE = "CopyDocs"
WINDOW_X_DIMENSION = 800
WINDOW_Y_DIMENSION = 500

root = tk.Tk()
root.title(f"{APP_TITLE}")
root.geometry(f"{WINDOW_X_DIMENSION}x{WINDOW_Y_DIMENSION}")
root.option_add("*tearOff", tk.FALSE)

MainWindow(root)

root.mainloop()
