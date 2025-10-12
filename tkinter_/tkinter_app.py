import pathlib
import tkinter as tk

import sv_ttk

from mainwindow import MainWindow

APP_TITLE = "CopyDocs"
WINDOW_X_DIMENSION = 800
WINDOW_Y_DIMENSION = 500

# theme_path = pathlib.Path(__file__).parent / "Forest-ttk-theme-master/forest-dark.tcl"
root = tk.Tk()

# root.call(
#     "source",
#     theme_path.as_posix(),
# )
# root.call("set_theme", "dark")

sv_ttk.set_theme("dark")

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
