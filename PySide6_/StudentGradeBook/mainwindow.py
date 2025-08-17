import enum

from PySide6.QtCore import Qt, QSize, Signal, Slot
from PySide6.QtGui import QColor, QPalette, QIcon
from PySide6.QtWidgets import (
    QMainWindow,
    QTableWidgetItem,
    QTableWidget,
    QAbstractButton,
    QLineEdit,
)

import validators
from PySide6_.StudentGradeBook.helpers import messagebox
from PySide6_.StudentGradeBook.models.customtablewidget import MyTableWidgetItem
from models import tablemodel
from ui.ui_mainwindow import Ui_MainWindow

TITLE = "Student Grade Book"

BUDDY_LABEL_RESET = QPalette.ColorRole.Text
VALID_FIELD = f"QLabel {{ {BUDDY_LABEL_RESET}; }}"
INVALID_EDIT = QColor(255, 255, 0, 125)

EDIT_ERROR_ICON = ":/resources/icons/warning.png"

SCORE_COLUMN = 2
FAILING_GRADE_THRESHOLD = 70
BAD_SCORE_COLOR = QColor(255, 0, 0, 150)
GOOD_SCORE_COLOR = QColor(0, 255, 0, 100)


class ItemState(enum.StrEnum):
    passing = "passing"
    failing = "failing"
    edit_error = "edit_error"


class ItemColor:
    passing = Qt.GlobalColor.transparent
    failing = Qt.GlobalColor.red
    edit_error = Qt.GlobalColor.yellow


# class MyTableWidgetItem(QTableWidgetItem):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._state = "uninitialized"
#
#     @property
#     def state(self):
#         return self._state
#
#     @state.setter
#     def state(self, new_state):
#         self._state = new_state


class MainWindow(Ui_MainWindow, QMainWindow):
    rows_changed = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(TITLE)
        self.resize(QSize(1200, 800))

        self.table_row_count = 0
        self.rows_changed.connect(self.toggle_clear_all_button_state)

        self.le_fields = [self.le_student_name, self.le_subject, self.le_score]
        self.buddy_labels = [self.lbl_student_name, self.lbl_subject, self.lbl_score]

        self.le_student_name_validator = validators.EmptyFieldValidator(
            self.le_student_name, self.lbl_student_name
        )
        self.le_subject_validator = validators.EmptyFieldValidator(
            self.le_subject, self.lbl_subject
        )
        self.le_score_validator = validators.IntValidator(
            self.le_score, self.lbl_score, 0, 100
        )

        self.validator_group = validators.ValidatorGroup(
            [
                self.le_student_name_validator,
                self.le_subject_validator,
                self.le_score_validator,
            ]
        )

        self.le_student_name.returnPressed.connect(
            self.le_student_name_validator.validate
        )
        self.le_student_name.editingFinished.connect(
            self.le_student_name_validator.validate
        )

        self.le_subject.returnPressed.connect(self.le_subject_validator.validate)
        self.le_subject.editingFinished.connect(self.le_subject_validator.validate)

        self.le_score.returnPressed.connect(self.le_score_validator.validate)
        self.le_score.textChanged.connect(self.le_score_validator.validate)

        self.tableWidget.itemChanged.connect(self.on_table_widget_item_changed)
        self.tableWidget.itemDelegate().closeEditor.connect(
            lambda edit_widget, _: self.on_close_editor_validate_edit(
                edit_widget, self.tableWidget.currentItem()
            )
        )

        self.pb_add_student.clicked.connect(self.add_student)
        self.pb_clear_all.clicked.connect(self.on_pb_clear_all_clicked)
        self.pb_clear_all.setEnabled(False)

    def add_student(self):
        self.validator_group.validate()

        if self.validator_group.is_valid:
            column_count = self.tableWidget.columnCount()
            new_row = self.add_row(self.tableWidget)

            for column in range(column_count):
                item = self.tableWidget.item(new_row, column)
                item.setText(self.le_fields[column].text())

                if column != SCORE_COLUMN:
                    # all cells are non-editable, except for the score cell
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                else:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    font = item.font()
                    font.setBold(True)
                    item.setFont(font)
                    self.color_score(item)

            self.clear_fields()
            self.update_average_score()
            self.le_student_name.setFocus()
            self.rows_changed.emit(self.table_row_count)

    def add_row(self, table_widget: QTableWidget) -> int:
        new_row = tablemodel.add_row(table_widget, table_widget.columnCount())
        self.table_row_count = table_widget.rowCount()
        self.rows_changed.emit(self.table_row_count)
        return new_row

    def update_average_score(self):
        row_count = self.tableWidget.rowCount()
        self.lbl_average_score.setStyleSheet(VALID_FIELD)

        sum_ = 0
        for row in range(row_count):
            item = self.tableWidget.item(row, SCORE_COLUMN)
            sum_ += int(item.text())

            if item.state == ItemState.edit_error:
                self.lbl_average_score.setStyleSheet("QLabel { color: yellow; }")

        average = sum_ / row_count
        self.lbl_average_score.setText(f"Average Score: {average:.02f}")

    def clear_fields(self):
        for line_edit, label in zip(self.le_fields, self.buddy_labels):
            line_edit.clear()
            label.setStyleSheet(VALID_FIELD)

    def toggle_clear_all_button_state(self, row_count: int):
        enable = False
        if row_count:
            enable = True
        self.pb_clear_all.setEnabled(enable)

    def on_pb_clear_all_clicked(self, _):
        @Slot(QAbstractButton)
        def clear_all_table_entries(button: QAbstractButton):
            # receives the buttonClicked signal when using messagebox functions to pop QMessageBoxs with .open()
            if "yes" in button.text().lower():
                self.tableWidget.clearContents()
                for row in range(self.tableWidget.rowCount()):
                    self.tableWidget.removeRow(row)

                self.lbl_average_score.setStyleSheet(VALID_FIELD)
                self.lbl_average_score.setText("Average Score: 0.00")

                self.clear_fields()
                self.rows_changed.emit(self.table_row_count)

        messagebox.question(
            self,
            "Reset Table",
            "Are you sure you want to remove all records?",
            clear_all_table_entries,
        )

    def on_table_widget_item_changed(self, item: MyTableWidgetItem):
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

        self.update_average_score()

    def on_close_editor_validate_edit(self, widget: QLineEdit, item: MyTableWidgetItem):
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

        self.update_average_score()

    @staticmethod
    def color_score(item: QTableWidgetItem):
        if int(item.text()) <= FAILING_GRADE_THRESHOLD:
            item.setBackground(BAD_SCORE_COLOR)
            return
        item.setBackground(GOOD_SCORE_COLOR)

    # @staticmethod
    # def is_valid_score(score: str) -> bool:
    #     try:
    #         score_ = int(score)
    #     except ValueError:
    #         return False
    #
    #     if score_ < 0 or score_ > 100:
    #         return False
    #
    #     return True
