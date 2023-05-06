from node import Node
from lifo import Lifo


def main() -> None:
    lifo: Lifo = Lifo()

    for x in range(10):
        lifo.append(x + 1)

    for x in range(11):
        print(lifo)
        try:
            lifo.popValue()
        except Exception as e:
            print(e)

    lifo.append(13)
    print(lifo)


if __name__ == "__main__":
    main()
