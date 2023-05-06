from __future__ import annotations


class Node:
    def __init__(self, value: int = 0, index: int = -1, next: Node = None, showIndex: bool = False) -> Node:
        self._value = value
        self._index = index
        self._next = next
        self._showIndex = showIndex

    def __str__(self) -> str:
        return self._print()

    def __repr__(self) -> str:
        return self._print()

    # private funcs
    def _print(self) -> str:
        return_str = ''

        if self._index != -1 and self._showIndex:
            return_str += f'[{self._index}] '

        return return_str + f'{self._value}'

    # setters & getters
    def setValue(self, newValue: int) -> None:
        self._value = newValue

    def getValue(self) -> int:
        return self._value

    def setIndex(self, newIndex: int) -> None:
        self._index = newIndex

    def getIndex(self) -> int:
        return self._index

    def setShowIndex(self, newShowIndex: bool) -> None:
        self._showIndex = newShowIndex

    def resetNext(self) -> None:
        self._next = None

    def setNext(self, newNext: Node) -> None:
        self._next = newNext

    def getNext(self) -> Node:
        return self._next

    # public funcs
    def print(self) -> str:
        return self._print()


if __name__ == "__main__":
    pass
