import sys

# noinspection PyUnresolvedReferences
import resources_rc  # noqa: F401
from mainwindow import MainWindow
from PySide6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
