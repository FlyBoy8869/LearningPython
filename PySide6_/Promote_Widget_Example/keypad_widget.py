from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame

from ui_keypad_widget import Ui_keypad


class KeyPadWidget(Ui_keypad, QFrame):
    keypress = Signal(str)
    limit: int = 10

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.frequency: list = []

        buttons = [
            (self.tb_zero, "0"),
            (self.tb_one, "1"),
            (self.tb_two, "2"),
            (self.tb_three, "3"),
            (self.tb_four, "4"),
            (self.tb_five, "5"),
            (self.tb_six, "6"),
            (self.tb_seven, "7"),
            (self.tb_eight, "8"),
            (self.tb_nine, "9"),
            (self.tb_decimal_point, "."),
        ]

        for button, data in buttons:
            button.clicked.connect(lambda _, d=data: self.update_frequency(d))

        self.tb_backspace.clicked.connect(self.remove_char)

    def update_frequency(self, char: str):
        if len(self.frequency) >= self.limit:
            return
        self.frequency.append(char)
        self.update_readout()

    def remove_char(self):
        if len(self.frequency) >= 1:
            self.frequency.pop()
            self.update_readout()

    def update_readout(self):
        self.readout.setText("".join(self.frequency))
