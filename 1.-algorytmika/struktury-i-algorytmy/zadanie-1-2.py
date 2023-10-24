# sprawdzanie czy liczba jest liczba pierwsza
import time


def current_milli_time():
    return round(time.time() * 1000)


def sprawdz_czy_pierwsza(liczba: int) -> bool:
    if liczba <= 1:
        return False

    for x in range(2, liczba):
        if liczba % x == 0:
            return False
    return True


def sprawdz_czy_pierwsza_optymalna(liczba: int) -> bool:
    if liczba <= 1:
        return False

    pierwiastek = liczba ** (1 / 2)
    for x in range(2, round(pierwiastek)):
        if liczba % x == 0:
            return False
    return True


cache: dict[int, bool] = {}
def sprawdz_czy_pierwsza_optymalna_z_cache(liczba: int) -> bool:
    try:
        return cache[liczba]
    except KeyError:
        if liczba <= 1:
            return False

        pierwiastek = liczba ** (1 / 2)
        for x in range(2, round(pierwiastek)):
            if liczba % x == 0:
                cache[liczba] = False
                return False

        cache[liczba] = True
        return True


def main():
    duza_liczba = 1_313_131_345_364_123

    start = current_milli_time()
    # print(sprawdz_czy_pierwsza(duza_liczba))  # True
    print(sprawdz_czy_pierwsza_optymalna(duza_liczba))  # True
    print(sprawdz_czy_pierwsza_optymalna(duza_liczba))  # True
    print(sprawdz_czy_pierwsza_optymalna(duza_liczba))  # True
    print(sprawdz_czy_pierwsza_optymalna(duza_liczba))  # True
    print(sprawdz_czy_pierwsza_optymalna(duza_liczba))  # True
    end = current_milli_time()
    print(end - start)

    start = current_milli_time()
    # print(sprawdz_czy_pierwsza(duza_liczba))  # True
    print(sprawdz_czy_pierwsza_optymalna_z_cache(duza_liczba))  # True
    print(sprawdz_czy_pierwsza_optymalna_z_cache(duza_liczba))  # True
    print(sprawdz_czy_pierwsza_optymalna_z_cache(duza_liczba))  # True
    print(sprawdz_czy_pierwsza_optymalna_z_cache(duza_liczba))  # True
    print(sprawdz_czy_pierwsza_optymalna_z_cache(duza_liczba))  # True
    end = current_milli_time()
    print(end - start)


main()
