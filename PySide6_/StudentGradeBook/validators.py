from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QLineEdit, QLabel


class FieldValidator:
    INVALID_FIELD = "QLabel { color: red; }"
    VALID_FIELD = f"QLabel {{ {QPalette.ColorRole.Text}; }}"

    def __init__(self, field: QLineEdit, buddy_label: QLabel):
        self.field = field
        self.label = buddy_label
        self._is_valid = False

    @property
    def is_valid(self):
        return self._is_valid

    def validate(self): ...


class EmptyFieldValidator(FieldValidator):
    def validate(self):
        if self.field.text() == "":
            self.label.setStyleSheet(self.INVALID_FIELD)
            self._is_valid = False
        else:
            self.label.setStyleSheet(self.VALID_FIELD)
            self._is_valid = True


class IntValidator(EmptyFieldValidator):
    def __init__(self, field: QLineEdit, buddy_label: QLabel, bottom: int, top: int):
        super().__init__(field, buddy_label)
        self.bottom = bottom
        self.top = top

    def validate(self):
        super().validate()

        try:
            integer = int(self.field.text())
        except ValueError:
            self.label.setStyleSheet(self.INVALID_FIELD)
            self._is_valid = False
            return

        if integer < self.bottom or integer > self.top:
            self.label.setStyleSheet(self.INVALID_FIELD)
            self._is_valid = False
            return

        self.field.setStyleSheet(self.VALID_FIELD)


class ValidatorGroup:
    def __init__(self, group: list[FieldValidator]):
        self.group = group

    @property
    def is_valid(self):
        return all([member.is_valid for member in self.group])

    def validate(self):
        for member in self.group:
            member.validate()
