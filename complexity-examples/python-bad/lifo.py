from __future__ import annotations
from node import Node


class Lifo:
    def __init__(self, showIndex: bool = False) -> Lifo:
        self._head = None
        self._tail = None
        self._index = -1
        self._showIndex = showIndex

    def __repr__(self) -> str:
        return self._print()

    def __str__(self) -> str:
        return self._print()

    # private funcs
    def _print(self) -> str:
        walker: Node = self._head

        return_str = '['
        while walker != None:
            return_str += f'{walker}'
            if walker.getNext() != None:
                return_str += ', '

            walker = walker.getNext()
        return_str += ']'

        return return_str

    def _append(self, node: Node) -> None:
        if self._head is None:
            self._head = node
            self._tail = self._head
            self._fixIndexes()
            return

        self._tail.setNext(node)
        self._tail = self._tail.getNext()
        self._fixIndexes()

    def _fixIndexes(self) -> None:
        self._index = -1
        walker: Node = self._head

        while walker != None:
            self._index += 1
            walker.setIndex(self._index)
            walker.setShowIndex(self._showIndex)
            walker = walker.getNext()

    # public funcs
    def append(self, node: Node) -> None:
        self._append(node)

    def append(self, value: int) -> None:
        node = Node(value=value, showIndex=self._showIndex)
        self._append(node)

    def popNode(self) -> Node:
        if self._tail == None or self._head == None:
            raise Exception("No more elements to pop")

        if self._tail == self._head:
            temp: Node = self._head
            self._head = None
            self._tail = None
            temp.resetNext()
            return temp

        temp: Node = self._tail
        walker: Node = self._head
        while walker.getNext() != temp:
            walker = walker.getNext()

        self._tail = walker
        self._tail.resetNext()
        temp.resetNext()
        return temp

    def popValue(self) -> int:
        return self.popNode().getValue()


if __name__ == "__main__":
    pass
