from functools import wraps
from icecream import ic
from loguru import logger

ic.configureOutput(includeContext=True)


def unique(func):
    @wraps(func)
    def wrapper(self, value):
        if value not in self.container:
            func(self, value)
            return
        logger.debug(f"prevented adding duplicate value: {value}")

    return wrapper


class MyList:
    def __init__(self):
        self.container = []

    @unique
    def add(self, value):
        self.container.append(value)


my_list = MyList()
my_list.add(1)
my_list.add(1)
print(my_list.container)
my_list.add(5)
my_list.add(1)
print(my_list.container)
