from PySide6.QtCore import QEvent, Qt
from PySide6.QtWidgets import QMainWindow

from ui_mainwindow import Ui_MainWindow
from aboutdialog import AboutDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.installEventFilter(self)

        self.actionAbout.triggered.connect(self.show_about)

    def show_about(self) -> None:
        dialog = AboutDialog(self, 400)
        dialog.exec()

    def eventFilter(self, obj, event: QEvent) -> bool:
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key.Key_H:  # noqa
            self.show_about()
            event.accept()
            return event.isAccepted()

        return super().eventFilter(obj, event)
