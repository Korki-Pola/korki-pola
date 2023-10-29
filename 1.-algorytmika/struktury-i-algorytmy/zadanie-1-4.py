cache: dict[int, bool] = {}


def czy_pierwsza_cache(liczba: int) -> bool:
    try:
        return cache[liczba]
    except KeyError:
        if liczba <= 1:
            return False

        pierwiastek = liczba ** (1 / 2)
        for x in range(2, round(pierwiastek) + 1):
            if liczba % x == 0:
                cache[liczba] = False
                return False

        cache[liczba] = True
        return True


def sito_arystotelesa(x: int) -> list[int]:
    liczby = []
    for liczba in range(x + 1):
        liczby.append(liczba)

    for indeks in range(len(liczby)):
        liczba = liczby[indeks]

        if liczba == None:
            continue

        if not czy_pierwsza_cache(liczba):
            liczby[indeks] = None
        else:
            for j in range(indeks + liczba, len(liczby), liczba):
                liczby[j] = None

    liczby_pierwsze = []
    for liczba in liczby:
        if liczba != None:
            liczby_pierwsze.append(liczba)

    return liczby_pierwsze


def czynniki_pierwsze(x: int):
    liczby_pierwsze = sito_arystotelesa(x // 2)

    if czy_pierwsza_cache(x):
        return [x]

    czynniki = []
    indeks = 0
    while x != 1:
        pierwsza = liczby_pierwsze[indeks]
        if x % pierwsza == 0:
            czynniki.append(pierwsza)
            x //= pierwsza
        else:
            indeks += 1

    return czynniki


# powinno wypisac [2, 2, 2, 2]
x = 2 ** 10
print(f'czynniki pierwsze {x}: {czynniki_pierwsze(x)}')
