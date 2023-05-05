def main() -> None:
    lifo = []

    for x in range(10):
        lifo.append(x + 1)

    for x in range(11):
        print(lifo)
        try:
            lifo.pop()
        except Exception as e:
            print(e)

    lifo.append(13)
    print(lifo)

    pass


if __name__ == "__main__":
    main()
