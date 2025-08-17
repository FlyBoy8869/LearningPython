from PySide6.QtWidgets import QDialog

from ui_mainview import Ui_MainView


class MainView(Ui_MainView, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.keypad.keypress.connect(lambda d: print(f"{d}", end=""))
