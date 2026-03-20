from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow

from ui_mainwindow import Ui_MainWindow
from aboutdialog import AboutDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.actionAbout.triggered.connect(self.show_about)

    def show_about(self) -> None:
        dialog = AboutDialog(self)
        dialog.exec()
