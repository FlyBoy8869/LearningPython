import tkinter as tk

from mainwindow import MainWindow

APP_TITLE = "CopyDocs"
WINDOW_X_DIMENSION = 800
WINDOW_Y_DIMENSION = 500

root = tk.Tk()

root.call(
    "source",
    r"C:\Users\charl\PycharmProjects\LearningPython\tkinter_\Sun-Valley-ttk-theme-master\Sun-Valley-ttk-theme-master\sun-valley.tcl",
)
root.call("set_theme", "dark")

root.title(f"{APP_TITLE}")
root.update_idletasks()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (WINDOW_X_DIMENSION // 2)
y = (screen_height // 2) - (WINDOW_Y_DIMENSION // 2)
root.geometry(f"{WINDOW_X_DIMENSION}x{WINDOW_Y_DIMENSION}+{x}+{y - (int(y * .5))}")

root.option_add("*tearOff", tk.FALSE)

MainWindow(root)

root.mainloop()
