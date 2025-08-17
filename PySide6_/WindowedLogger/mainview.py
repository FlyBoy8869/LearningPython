from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QDialog, QPushButton, QTextEdit, QVBoxLayout
from loguru import logger

from windowedlogger import WindowedLogger


class MainView(QDialog):
    def __init__(self):
        self.windowed_logger = WindowedLogger()

        logger.remove()
        logger.add(self.windowed_logger, level="TRACE")

        super().__init__()
        self.resize(QSize(600, 300))

        layout = QVBoxLayout()

        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        self.pb_trouble = QPushButton("Cause Trouble")
        # self.pb_trouble.setAutoDefault(False)
        self.pb_trouble.clicked.connect(self.cause_trouble)
        layout.addWidget(self.pb_trouble)

        self.setLayout(layout)

    @logger.catch
    def cause_trouble(self) -> None:
        a = 1
        b = 0
        print(a / b)

    def keyPressEvent(self, event, /) -> None:  # noqa: N802
        modifiers: Qt.KeyboardModifier = (
            Qt.KeyboardModifier.ControlModifier | Qt.KeyboardModifier.ShiftModifier
        )
        if event.key() == Qt.Key.Key_L and event.modifiers() == modifiers:
            self._show_log_view()

    def _show_log_view(self) -> None:
        if self.windowed_logger.isHidden():
            logger.trace("showing log view")
            self.windowed_logger.open()
