from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMessageBox

QUESTION_ICON = ":/resources/icons/question-circle-100x100.png"
WARNING_ICON = ":/resources/icons/warning-128x128.png"


def question(
    parent,
    title: str,
    text: str,
    callback,
    buttons: QMessageBox.StandardButton = QMessageBox.StandardButton.No
    | QMessageBox.StandardButton.Yes,
    icon: str = QUESTION_ICON,
):
    return _show_message_box(parent, title, text, callback, buttons, icon)


def warning(
    parent,
    title: str,
    text: str,
    callback,
    buttons: QMessageBox.StandardButton = QMessageBox.StandardButton.Ok,
    icon: str = WARNING_ICON,
):
    return _show_message_box(parent, title, text, callback, buttons, icon)


def _show_message_box(
    parent,
    title: str,
    text: str,
    callback,
    buttons: QMessageBox.StandardButton,
    icon: str,
):
    message_box = QMessageBox(QMessageBox.Icon.NoIcon, title, text, buttons, parent)
    message_box.setIconPixmap(QPixmap(icon))
    message_box.buttonClicked.connect(callback)
    return message_box.open()
