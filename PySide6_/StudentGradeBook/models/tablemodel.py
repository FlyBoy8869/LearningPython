from PySide6.QtWidgets import QTableWidget

from .customtablewidget import MyTableWidgetItem


def add_row(table: QTableWidget, column_count: int) -> int:
    row_count = table.rowCount()
    table.insertRow(row_count)

    for col in range(column_count):
        item = MyTableWidgetItem()
        table.setItem(row_count, col, item)

    return row_count
