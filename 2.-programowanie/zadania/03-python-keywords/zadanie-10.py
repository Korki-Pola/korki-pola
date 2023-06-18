liczba = int(input("Wpisz liczbę: "))
for i in range(1, liczba + 1):
    print(" " * (liczba - i) + "*" * (2 * i - 1))

    # spacje = ' ' * (liczba - i)
    # gwiazdki = '*' * (2 * i - 1)
    # print(f'{spacje}{gwiazdki}')

    # gwiazdki = '*' * (2 * i - 1)
    # print(f'{gwiazdki:>{len(gwiazdki) + (liczba - i)}}')
