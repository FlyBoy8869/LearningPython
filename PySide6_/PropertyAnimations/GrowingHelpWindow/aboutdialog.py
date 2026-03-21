from PySide6.QtCore import QPropertyAnimation, QSize, QEvent, Qt
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QDialog

from ui_about import Ui_About


class AboutDialog(QDialog, Ui_About):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.installEventFilter(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)

        p = QPalette()
        color: str = p.color(QPalette.ColorRole.Window).name(QColor.NameFormat.HexArgb)
        dialog_stylesheet: str = (
            f"QWidget {{background-color: {color}; border-width: 4px; border-style: solid; border-radius: 20px; border-color: #7393B3;}}"
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet(dialog_stylesheet)

        self.move(parent.pos())

        self.size_animation = QPropertyAnimation(self, b"size")
        self.size_animation.setEndValue(QSize(parent.width(), 300))
        self.size_animation.setDuration(150)
        self.size_animation.start()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            self.close()
            event.accept()
            return event.isAccepted()

        return super().eventFilter(obj, event)
