from PySide6.QtCore import QSize, Qt, QTimer
from PySide6.QtWidgets import QDialog, QScrollBar, QTextEdit, QVBoxLayout

from protocols import Writeable

Y_SCOLL_TO_TOP_THRESHOLD = 10
Y_SCROLL_TO_BOTTOM_THRESHOLD = 10


class WindowedLogger(QDialog):
    """
    Write log messages to a dialog window in GUI applications where a terminal is not available.

    The display area can be scrolled to the top or bottom
    by clicking the top edge or bottom edge of the client area, respectively.
    """

    def __init__(self, *, width: int = 700, height: int = 200):
        super().__init__()
        self.setWindowTitle("Windowed Logger")
        self.setWindowFlags(Qt.WindowType.Tool)
        self.resize(QSize(width, height))

        layout = QVBoxLayout()

        self.log_display = QTextEdit(self)
        self.log_display.setReadOnly(True)

        layout.addWidget(self.log_display)
        self.setLayout(layout)

        self.buffer: list = []

    @property
    def sink(self) -> Writeable:
        return self

    def write(self, log_message: str) -> None:
        self.buffer.append(log_message)
        self.log_display.append(log_message.strip())

    def mouseReleaseEvent(self, event, /) -> None:  # noqa: N802
        def do_visual() -> None:
            self.setWindowTitle(f"{self.windowTitle()} - scrolling...")
            QTimer.singleShot(300, self, lambda: self.setWindowTitle("Windowed Logger"))

        mouse_y: int = event.pos().y()
        v_scrollbar: QScrollBar = self.log_display.verticalScrollBar()

        if mouse_y <= Y_SCOLL_TO_TOP_THRESHOLD:
            do_visual()
            v_scrollbar.setValue(v_scrollbar.minimum())
        elif self.height() - mouse_y <= Y_SCROLL_TO_BOTTOM_THRESHOLD:
            do_visual()
            v_scrollbar.setValue(v_scrollbar.maximum())
