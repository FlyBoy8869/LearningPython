from pathlib import Path
from random import choice

from PySide6.QtCore import QPoint, QSize, Qt
from PySide6.QtGui import QKeyEvent, QPainter, QPixmap
from PySide6.QtWidgets import QApplication, QDialog

from ui_mainwindow import Ui_MainView

image_files: Path = Path(__file__).parent

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800


def scoop_up_image_files(folder: str | Path) -> list[Path]:
    path = Path(folder)
    pictures: list[Path] = []
    extensions: list[str] = ["jpg", "png", "bmp", "gif"]

    for extension in extensions:
        pictures.extend(
            path.glob(f"*.{extension}", case_sensitive=False),
        )

    return pictures


class MainView(Ui_MainView, QDialog):
    picture_names: list[Path] = scoop_up_image_files(image_files)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(QSize(WINDOW_WIDTH, WINDOW_HEIGHT))
        # self.draw_random_pic()
        self.show_random_picture()

    def keyReleaseEvent(self, event: QKeyEvent) -> None:  # noqa: N802
        if event.key() == Qt.Key.Key_Space:
            self.show_random_picture()
            return
        super().keyReleaseEvent(event)

    def draw_random_pic(self) -> None:
        picture: QPixmap = QPixmap(
            str(image_files / choice(self.picture_names))
        ).scaled(
            600,
            800,
            aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
        )
        pic_width: int = picture.width()
        pic_height: int = picture.height()
        self.resize(QSize(pic_width, pic_height))
        self.canvas.setPixmap(QPixmap(pic_width, pic_height))
        self.draw_picture(picture)

    def show_random_picture(self) -> None:
        selected_picture: Path = image_files / choice(self.picture_names)
        self.setWindowTitle(f"{selected_picture.name}")
        picture: QPixmap = QPixmap(str(selected_picture)).scaled(
            600,
            800,
            aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
        )
        pic_width: int = picture.width()
        pic_height: int = picture.height()
        self.resize(QSize(pic_width, pic_height))
        self.canvas.setPixmap(picture)

    def draw_picture(self, picture) -> None:
        canvas: QPixmap = self.canvas.pixmap()
        painter = QPainter(canvas)
        painter.drawPixmap(QPoint(0, 0), picture)
        painter.end()
        self.canvas.setPixmap(canvas)
        self.update()


if __name__ == "__main__":
    app = QApplication()
    window = MainView()
    window.show()
    app.exec()
