import sys
from typing import NoReturn

from mainwindow import MainWindow
from PySide6.QtWidgets import QApplication


def main() -> NoReturn:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
