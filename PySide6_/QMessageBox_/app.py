import platform

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QMessageBox,
)


def handle_button_click(parent, icon: QPixmap, title: str, message: str):
    mbox = QMessageBox(parent)
    # mbox.setIconPixmap(QPixmap("stop-alert_512x512.png"))
    mbox.setIconPixmap(icon)
    mbox.setWindowTitle(title)
    mbox.setInformativeText(message)
    mbox.setText(title)
    mbox.open()


app = QApplication([])

if "windows" in platform.platform().lower():
    import qdarkstyle

    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyside6"))

window = QWidget()
window.setWindowFlag(window.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
window.setWindowTitle("A PySide6_Examples Example")

v_layout = QVBoxLayout(window)
v_layout.addStretch()

button = QPushButton("Warning")
button.clicked.connect(
    lambda _: handle_button_click(
        window,
        QPixmap("resources/warning-triangle-yellow.png"),
        "Warning",
        "Hydrogen Extractor temperature is rising.",
    )
)
v_layout.addWidget(button)

cw_button = QPushButton("Warning - Critical")
cw_button.clicked.connect(
    lambda _: handle_button_click(
        window,
        QPixmap("resources/images/critical-alert_512x512.png"),
        "Warning: Critical",
        "Hydrogen Extractor in thermal runaway!!!",
    )
)
v_layout.addWidget(cw_button)

v_layout.addStretch()

window.resize(QSize(250, 100))

window.show()

app.exec()
