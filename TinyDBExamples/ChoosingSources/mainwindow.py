from typing import TYPE_CHECKING

import database as db
import messages
from PySide6.QtWidgets import QFileDialog, QMainWindow, QMenu
from ui_mainwindow import Ui_MainWindow

if TYPE_CHECKING:
    from PySide6.QtGui import QCloseEvent


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_menu_actions()

        self.actionExit.triggered.connect(self.close)

        self.load_sources()
        self.listWidget.itemClicked.connect(self.handle_listwidget_item_clicked)

    def closeEvent(self, event: QCloseEvent) -> None:  # noqa: N802
        db.close()
        return super().closeEvent(event)

    def handle_action_add_source(self, _) -> None:
        if directory := QFileDialog.getExistingDirectory(
            self,
            "Select a document source",
        ):
            if db.has_source(directory):
                messages.warning_ok("Source already in database.", self)
                return

            self.listWidget.addItem(directory)
            db.add_source(directory)

    def handle_listwidget_item_clicked(self, item) -> None:
        print(f"{item.text()} at row {self.listWidget.row(item)}")

    def handle_view_sources(self, _) -> None:
        from pprint import pprint  # noqa: PLC0415

        pprint(db.sources())

    def add_menu_actions(self) -> None:
        sources_menu = QMenu(self, title="Document Sources")
        sources_menu.addAction("Add Source").triggered.connect(
            self.handle_action_add_source,
        )
        sources_menu.addAction("View Sources").triggered.connect(
            self.handle_view_sources,
        )
        self.menuSettings.addMenu(sources_menu)

    def load_sources(self) -> None:
        self.listWidget.addItems(db.sources())
