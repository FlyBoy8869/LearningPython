"""Example of promoting a stock widget to a custom widget in Qt Designer."""

import sys

from mainview import MainView
from PySide6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    window = MainView()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
