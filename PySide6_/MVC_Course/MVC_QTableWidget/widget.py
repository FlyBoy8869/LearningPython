import csv
import datetime
import time

import humanize
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget

from models import tablemodel
from ui_widget import Ui_Widget

DATAFILE = "products-10000.csv"


class Widget(Ui_Widget, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(QSize(2000, 500))

        self.header_alignments = [
            Qt.AlignmentFlag.AlignLeft,
            Qt.AlignmentFlag.AlignCenter,
            Qt.AlignmentFlag.AlignRight,
        ]

        start = time.time()
        with open(DATAFILE, "r") as csv_file:
            reader = csv.reader(csv_file)
            self.headers = next(reader)

            self.tableWidget.setColumnCount(len(self.headers))
            self.tableWidget.setHorizontalHeaderLabels(self.headers)
            self.tableWidget.setStyleSheet("QTableWidget::item { padding-left: 10px; }")

            for row, data in enumerate(reader):
                tablemodel.add_row(self.tableWidget, self.tableWidget.columnCount())
                for col in range(len(self.headers)):
                    self.tableWidget.item(row, col).setText(data[col])

        elapsed = time.time() - start
        print(
            f"populating table took {humanize.precisedelta(datetime.timedelta(seconds=elapsed), minimum_unit="milliseconds")}"
        )
