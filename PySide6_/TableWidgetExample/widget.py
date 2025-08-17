import enum
import random
import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLineEdit, QTableWidgetItem, QWidget

from ui_widget import Ui_Widget

FAILING_GRADE_THRESHOLD = 70
EDIT_ERROR_ICON = ":/warning.png"


class ItemState(enum.StrEnum):
    passing = "passing"
    failing = "failing"
    edit_error = "edit_error"


class ItemColor:
    passing = Qt.GlobalColor.transparent
    failing = Qt.GlobalColor.red
    edit_error = Qt.GlobalColor.yellow


class MyTableWidgetItem(QTableWidgetItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._state = "uninitialized"

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state


class Widget(Ui_Widget, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("TableWidget Example")
        self.edit = False

        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(5)

        self.tableWidget.itemDelegate().closeEditor.connect(
            lambda widget, _: self.on_close_editor_validate_edit(
                widget, self.tableWidget.currentItem()
            )
        )
        self.tableWidget.itemChanged.connect(self.on_table_widget_item_changed)

        self.fill_table(None)

        self.pb_fill_table.clicked.connect(self.fill_table)

    @Slot()
    def fill_table(self, _):
        self.tableWidget.clearContents()

        for row in range(5):
            for col in range(6):
                item = MyTableWidgetItem(row, col)
                grade = random.randint(0, 100)
                item.state = (
                    ItemState.failing
                    if grade < FAILING_GRADE_THRESHOLD
                    else ItemState.passing
                )
                item.setText(f"{grade}")
                self.tableWidget.setItem(row, col, item)

    @staticmethod
    def on_table_widget_item_changed(item: MyTableWidgetItem):
        if item.state == ItemState.edit_error:
            return

        try:
            grade = int(item.text())
        except ValueError:
            # ignore edit errors; QTableWidget.itemChanged is called for every change to a cell
            # this condition is handled in 'on_close_editor_validate_edit'
            return

        state = ItemState.passing
        color = ItemColor.passing

        if grade < FAILING_GRADE_THRESHOLD:
            state = ItemState.failing
            color = ItemColor.failing

        item.state = state
        item.setBackground(color)

    @staticmethod
    def on_close_editor_validate_edit(widget: QLineEdit, item: MyTableWidgetItem):
        state = ItemState.passing
        color = ItemColor.passing

        try:
            new_grade = int(widget.text())
            item.setIcon(QIcon())
            if new_grade < FAILING_GRADE_THRESHOLD:
                state = ItemState.failing
                color = ItemColor.failing
        except ValueError:
            state = ItemState.edit_error
            color = ItemColor.edit_error
            item.setIcon(QIcon(EDIT_ERROR_ICON))
            item.setText("0")

        item.state = state
        item.setBackground(color)


def main():
    app = QApplication(sys.argv)
    window = Widget()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
