import sys
from pathlib import Path

import cdcutilities
from PySide6.QtCore import QRectF, Qt, QTimer, Signal
from PySide6.QtGui import QFont, QFontDatabase, QPainter, QPen, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
)

# constants for displaying the countdown timer
POINT_SIZE = 50
FONT = "Roboto-VariableFont_wdth,wght.ttf"
FONT_PATH = Path.cwd() / FONT
FONT_FAMILY_DEFAULT = ".AppleSystemUIFont"

COUNT_COLOR = Qt.GlobalColor.yellow

# constants for displaying the countdown ring
PEN_WIDTH = 7
PEN_COLOR = Qt.GlobalColor.green
PEN_CAP_STYLE = Qt.PenCapStyle.MPenCapStyle
PEN_LINE_STYLE = Qt.PenStyle.SolidLine
PEN_JOIN_STYLE = Qt.PenJoinStyle.RoundJoin

CANVAS_FILL_COLOR = Qt.GlobalColor.black

# countdown time
SECONDS = 3600


class MainView(QMainWindow):
    countdown_finished = Signal()

    def __init__(self, countdown, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"{countdown} sec. timer")
        self.countdown_finished.connect(self.on_countdown_finished)

        layout = QVBoxLayout()
        self.frame = QFrame()
        self.frame.setLayout(layout)

        self._countdown = countdown
        self.countdown = countdown
        self.counter = 0

        # arc stuff
        self.start_angle = 90.0 * 16.0
        self.angle_span = -(16.0 * 360.0)
        self.degree_delta = 16.0 * 360.0 / countdown
        print(f"{self.degree_delta=}")

        self.pen = QPen(
            PEN_COLOR, PEN_WIDTH, PEN_LINE_STYLE, PEN_CAP_STYLE, PEN_JOIN_STYLE
        )

        # set up the font
        font_family = FONT_FAMILY_DEFAULT
        font_id = QFontDatabase.addApplicationFont(str(FONT_PATH))
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        if font_families:
            font_family = font_families[0]
        self.font = QFont(font_family, POINT_SIZE, QFont.Weight.Bold)

        # the painting surface
        self.canvas = QPixmap(500, 500)
        self.label = QLabel()
        self.label.setPixmap(self.canvas)

        layout.addWidget(self.label)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_timer)
        layout.addWidget(self.start_button)

        self.setCentralWidget(self.frame)

        self.draw_countdown_circle()

        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timer_timeout)

    def on_countdown_finished(self):
        self.change_start_button_label("Start")

        self.counter = 0
        self.countdown = self._countdown
        self.start_angle = 90.0 * 16.0
        self.angle_span = -(16.0 * 360.0)
        self.degree_delta = 16.0 * 360.0 / self._countdown

        self.draw_countdown_circle()

    def on_timer_timeout(self):
        self.countdown -= 1
        self.counter += 1

        if self.countdown <= 0:
            self.timer.stop()
            QTimer.singleShot(1000, self.countdown_finished.emit)

        self.draw_countdown_circle()

    def draw_countdown_circle(self):
        self.canvas.fill(CANVAS_FILL_COLOR)

        self.pen.setColor(PEN_COLOR)
        painter = QPainter(self.canvas)
        painter.setPen(self.pen)

        new_x = self.canvas.rect().x() + PEN_WIDTH / 2
        new_y = self.canvas.rect().y() + PEN_WIDTH / 2
        new_height = self.canvas.rect().height() - PEN_WIDTH
        new_width = self.canvas.rect().width() - PEN_WIDTH

        # noinspection PyTypeChecker
        painter.drawArc(
            QRectF(new_x, new_y, new_height, new_width),
            self.start_angle,
            self.angle_span + (self.counter * self.degree_delta),
        )

        painter.setFont(self.font)

        text = cdcutilities.time.format_seconds(
            self.countdown, use_days=True, multi_line=False
        )

        self.pen.setColor(COUNT_COLOR)
        painter.setPen(self.pen)

        painter.drawText(
            self.canvas.rect(),
            Qt.AlignmentFlag.AlignCenter,
            text,
        )

        painter.end()

        self.label.setPixmap(self.canvas)

    def start_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.change_start_button_label("Start")
        else:
            self.timer.start(1000)
            self.change_start_button_label("Pause")

    def change_start_button_label(self, text):
        self.start_button.setText(text)


app = QApplication(sys.argv)
window = MainView(SECONDS)
window.show()

app.exec()
