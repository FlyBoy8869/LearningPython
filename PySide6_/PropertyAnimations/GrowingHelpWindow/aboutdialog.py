from PySide6.QtCore import QPropertyAnimation, QSize
from PySide6.QtWidgets import QDialog

from ui_about import Ui_About


class AboutDialog(QDialog, Ui_About):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.move(parent.pos())

        self.size_animation = QPropertyAnimation(self, b"size")
        self.size_animation.setEndValue(QSize(parent.width(), 300))
        self.size_animation.setDuration(150)
        self.size_animation.start()
