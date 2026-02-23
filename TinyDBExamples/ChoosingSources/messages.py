from PySide6.QtWidgets import QMessageBox, QWidget


def _make_message_instance(icon, title, text, buttons, parent) -> QMessageBox:
    return QMessageBox(
        icon,
        title,
        text,
        buttons,
        parent=parent,
    )


def warning_ok(text: str, parent: QWidget) -> None:
    """Displays a warning message box with an Ok button."""
    _make_message_instance(
        QMessageBox.Icon.Warning,
        "Warning",
        text,
        QMessageBox.StandardButton.Ok,
        parent,
    ).open()
