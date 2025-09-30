from typing import Any, Self


class Node:
    def __init__(self, value: Any):
        self.value: Any = value
        self.next: Self = None
        self.prev: Self = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length: int = 0

    def append(self, value):
        new_node: Node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            # Set the next property on the tail to be that node
            self.tail.next = new_node
            # Set the previous property on the newly created node to be the tail
            new_node.prev = self.tail
            # Set the tail to be the newly created node
            self.tail = new_node

        self.length += 1

        return self

    def print_forward(self, end="\n"):
        self.print_("forward", end)

    def print_backward(self, end="\n"):
        self.print_("backward", end)

    def print_(self, direction: str, end: str = "\n"):
        for value in self.walk_(direction):
            print(value, end=end)

    def walk_forward(self):
        yield from self.walk_("forward")

    def walk_backward(self):
        yield from self.walk_("backward")

    def walk_(self, direction: str):
        assert direction in ["forward", "backward"], f"invalid direction: '{direction}'"

        current: Node = self.head if direction == "forward" else self.tail
        while current:
            yield current.value
            current = current.next if direction == "forward" else current.prev

    def __str__(self):
        current: Node = self.head
        result: list[Any] = []
        while current:
            result.append(current.value)
            current = current.next
        return str(result)


if __name__ == "__main__":
    dll_1 = DoublyLinkedList()

    for i in range(1, 50):
        dll_1.append(i)

    dll_1.print_forward(end=" ")
    print()

    dll_1.print_backward(end=" ")
