class MySet:
    def __init__(self):
        self._data = dict()

    @property
    def items(self):
        return self._data.items()

    def add(self, item):
        self._data[item] = None

    def __iter__(self):
        return iter(self._data)

    def __str__(self):
        # return f"{[key for key in self._data.keys()]}"
        return f"{set(self._data.keys())}"


if __name__ == "__main__":
    myset1 = MySet()
    myset2 = MySet()

    myset1.add("Hello")
    myset1.add("World")
    print(myset1)

    myset2.add("Apple")
    myset2.add("Banana")
    myset2.add("World")
    print(myset2)

