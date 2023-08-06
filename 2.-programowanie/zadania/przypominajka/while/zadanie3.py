# Liczby Parzyste: Wydrukuj liczby parzyste między 1 a 20 przy użyciu pętli while.
poczatkowa_liczba = 0
koncowa_liczba = 20
licznik = poczatkowa_liczba
while licznik < koncowa_liczba:
    nowy_licznik = licznik + 1
    if nowy_licznik % 2 == 0:
        print(nowy_licznik)
    licznik = nowy_licznik
