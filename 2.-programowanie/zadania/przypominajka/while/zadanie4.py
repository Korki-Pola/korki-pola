# Liczby Nieparzyste: Wydrukuj liczby nieparzyste między 1 a 20 przy 
# użyciu pętli while.
poczatkowa_liczba = 0
koncowa_liczba = 20
licznik = poczatkowa_liczba
while licznik < koncowa_liczba:
    if licznik % 2 == 1:
        print(licznik)
    licznik = licznik + 1
    