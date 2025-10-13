import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# noinspection PyTypeChecker,PyArgumentList
class MainWindow(ttk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.configure(padx=5, pady=5)

        self.main_frame = ttk.Frame(self, bootstyle=(SUCCESS,))
        self.main_frame.pack(side=LEFT, anchor=NW)

        self.button1 = ttk.Menubutton(
            self.main_frame, text="File", bootstyle=(PRIMARY,)
        )
        self.button1.pack(side=LEFT, anchor=NW)

        self.button2 = ttk.Menubutton(
            self.main_frame, text="Options", bootstyle=(PRIMARY,)
        )
        self.button2.pack(side=LEFT, anchor=NW)


app = MainWindow(themename="darkly")
app.geometry("640x480")
app.mainloop()
