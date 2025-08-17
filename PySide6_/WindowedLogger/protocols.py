from typing import Protocol


class Writeable(Protocol):
    def write(self, message) -> None: ...
