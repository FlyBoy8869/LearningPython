from typing import TYPE_CHECKING

import database as db
import messages
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from ui_manage_sources import Ui_Dialog

if TYPE_CHECKING:
    from PySide6.QtGui import QCloseEvent


class ManageSourcesDialog(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.load_sources()

        self.pb_add.clicked.connect(self.handle_action_add_source)
        self.pb_delete.clicked.connect(self.handle_delete_source)
        self.pb_close.clicked.connect(self.close)

    def closeEvent(self, event: QCloseEvent) -> None:  # noqa: N802
        return super().closeEvent(event)

    def handle_action_add_source(self, _) -> None:
        if directory := QFileDialog.getExistingDirectory(
            self,
            "Select a document source",
        ):
            if db.has_source(directory):
                messages.warning_ok("Source already in database.", self)
                return

            self.lw_sources.addItem(directory)
            db.add_source(directory)

    def handle_delete_source(self) -> None:
        if not self.lw_sources.count():
            return

        if QMessageBox.question(self, "Delete", "Are you sure?") == QMessageBox.StandardButton.Yes:
            db.delete_source(self.lw_sources.currentItem().text())
            self.lw_sources.takeItem(self.lw_sources.currentRow())


    def load_sources(self) -> None:
        self.lw_sources.addItems(db.sources())
