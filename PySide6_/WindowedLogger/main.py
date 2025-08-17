import sys

from PySide6.QtWidgets import QApplication

from mainview import MainView


def main() -> None:
    app = QApplication(sys.argv)

    main_view = MainView()
    main_view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
