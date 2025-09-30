from typing import Any, Sequence


class TKListItem(str):
    def __new__(cls, content: Sequence, extra: Any = None):
        # __new__ is used to create and return a new instance of the class
        # It's called before __init__ for immutable types like str
        obj = super().__new__(cls, content)
        obj.extra = extra  # Add custom attributes
        return obj

    def __init__(self, content, extra):
        # __init__ is called after __new__ to initialize the instance
        # For str subclasses, __init__ is typically less critical if __new__ handles the core string value
        # We don't call super().__init__ here as str's __init__ is often not intended for direct use
        pass


if __name__ == "__main__":
    list_item = TKListItem("Hello", ["one"])
    print(list_item)
    print(list_item.extra)
