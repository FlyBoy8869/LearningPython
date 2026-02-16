# validator.py

import sys
from pathlib import Path

from loguru import logger

logger.remove()
logger.add(sys.stderr, level="DEBUG")
logger.add(Path(__file__).parent / "debug.log", level="DEBUG", mode="w")


class StringValidator:
    def __init__(self, *, minsize, readonly=False):
        self.minsize = minsize
        self.readonly = readonly

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, name):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if self._name not in instance.__dict__ or not self.readonly:
            self.validate(value)
            instance.__dict__[self._name] = value
            return
        logger.warning(f"invalid attempt to write to readonly variable '{self._name}'")

    def validate(self, value):
        if not isinstance(value, str):
            msg = f"{value} must be a string"
            raise TypeError(msg)
        if len(value) < self.minsize:
            msg = f"'{self._name}' must be at least {self.minsize} characters long."
            raise ValueError(msg)


class Song:
    title = StringValidator(minsize=2)
    artist = StringValidator(minsize=3, readonly=True)

    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f"This is {self.title} by {self.artist}"

    def __repr__(self):
        return "Song(title: str, artists: str)"


if __name__ == "__main__":
    s1 = Song("A Forest", "The Cure")
    print(s1)

    s1.artist = "The Monkeys"
    print(s1)

    s2 = Song("Crazy Train", "Ozzy Osborne")
    print(s2)

    # print(dir(s2))

    s2.artist = "W"
    print(s2)
