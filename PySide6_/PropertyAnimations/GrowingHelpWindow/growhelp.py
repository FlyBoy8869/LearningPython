import sys

from PySide6.QtWidgets import QApplication

from mainwindow import MainWindow

app = QApplication([])
window = MainWindow()
window.show()

sys.exit(app.exec())
