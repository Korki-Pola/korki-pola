liczba = int(input("Wpisz liczbę: "))
for i in range(1, liczba + 1):
    print(" " * (liczba - i) + "*" * (2 * i - 1))