from typing import TYPE_CHECKING

import database as db
import messages
from PySide6.QtWidgets import QFileDialog, QMainWindow
from ui_mainwindow import Ui_MainWindow

if TYPE_CHECKING:
    from PySide6.QtGui import QCloseEvent, QShowEvent


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.actionExit.triggered.connect(self.close)
        self.actionSelect_Source.triggered.connect(self.handle_action_select_source)

    def closeEvent(self, event: QCloseEvent) -> None:  # noqa: N802
        db.close()
        return super().closeEvent(event)

    def showEvent(self, event: QShowEvent) -> None:  # noqa: N802
        self.load_sources()
        return super().showEvent(event)

    def handle_action_select_source(self, _) -> None:
        if directory := QFileDialog.getExistingDirectory(
            self,
            "Select a document source",
        ):
            if db.source_exists(directory):
                # msgbox = QMessageBox(
                #     QMessageBox.Icon.Warning,
                #     "Source",
                #     "Source already exists in the database.",
                #     QMessageBox.StandardButton.Ok,
                #     parent=self,
                # )
                # msgbox.open()
                messages.warning_ok("Source already in database.", self)
                return

            self.listWidget.addItem(directory)
            db.add_source(directory)

    def load_sources(self) -> None:
        if not len(db.sources_table):
            return

        for source in db.sources_table.all():
            self.listWidget.addItem(source["source"])
