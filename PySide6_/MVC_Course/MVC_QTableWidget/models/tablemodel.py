from PySide6.QtWidgets import QTableWidget, QTableWidgetItem


def add_row(table: QTableWidget, column_count: int) -> None:
    row_count = table.rowCount()
    table.insertRow(row_count)

    for col in range(column_count):
        item = QTableWidgetItem()
        table.setItem(row_count, col, item)
