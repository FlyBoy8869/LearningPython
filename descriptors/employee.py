# employee.py
from datetime import date


class Date:
    def __set_name__(self, _, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = date.fromisoformat(value)


class Employee:
    birth_date = Date()
    hire_date = Date()

    def __init__(self, name: str, birth_date: str, hire_date: str):
        self._name = name
        self.birth_date = birth_date
        self.hire_date = hire_date

    @property
    def name(self) -> str:
        return self._name


if __name__ == "__main__":
    e = Employee("Charles", "1969-05-22", "2010-01-10")
    print(f"{e.name} was hired on {e.hire_date}")
    print(f"{e.name}' birthday is {e.birth_date:%B %d, %Y}")
    # e.name = "Charles Cognato"  # raises AttributeError
    print(dir(e))
