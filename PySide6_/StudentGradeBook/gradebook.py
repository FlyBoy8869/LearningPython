import sys

from PySide6.QtWidgets import QApplication

# noinspection PyUnresolvedReferences
import resources_rc
from mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
