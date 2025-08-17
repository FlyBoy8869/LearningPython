from PySide6.QtWidgets import QWidget

from progress_widget_ui import Ui_ProgressWidget


class ProgressWidget(Ui_ProgressWidget, QWidget):
    def __init__(self, w_id: str, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.label.setText(f"JobID: [{w_id}]")
