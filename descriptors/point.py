# point.py

class Point:
    def __init__(self, x: int, y: int):
        self.x: float = x
        self.y: float = y

    def __getattr__(self, name: str) -> int:
        return self.__dict__[f"_{name}"]

    def __setattr__(self, name: str, value: int) -> None:
        self.__dict__[f"_{name}"] = float(value) + 5


if __name__ == "__main__":
    p = Point(5, 5)
    print(f"{p.x = }")
    p.z = 7
    print(f"{p.z = }")
