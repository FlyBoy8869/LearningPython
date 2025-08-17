"""Example of promoting a stock widget to a custom widget in Qt Designer."""

import sys

from PySide6.QtWidgets import QApplication

from mainview import MainView


def main():
    app = QApplication(sys.argv)
    window = MainView()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
