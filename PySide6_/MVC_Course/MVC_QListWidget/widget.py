from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget

from ui_widget import Ui_Widget

window_title = "Fruit List Demo"


class Widget(Ui_Widget, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        fruits = [
            "Apple",
            "Avocado",
            "Banana",
            "Blueberries",
            "Cucumber",
            "EggFruit",
            "Fig",
            "Grape",
            "Mango",
            "Pear",
            "Pineapple",
            "Watermellon",
        ]

        self.listWidget.addItems(fruits)

        for i in range(self.listWidget.count()):
            self.listWidget.item(i).setIcon(
                QIcon(QPixmap(f":/images/{fruits[i].lower()}.png").scaled(100, 100))
            )

        self.listWidget.itemClicked.connect(self.update_title_with_selection)
        self.pb_read_data.clicked.connect(self.on_pb_read_data_button_clicked)

    def update_title_with_selection(self, _) -> None:
        self.setWindowTitle(f"{window_title} - {self.listWidget.currentItem().text()}")

    def on_pb_read_data_button_clicked(self, _) -> None:
        current_item = self.listWidget.currentItem()
        data = current_item.data(Qt.ItemDataRole.DisplayRole)
        print(f"Current fruit: {data}")
