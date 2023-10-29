# sprawdzanie, czy liczba jest liczbą doskonałą

def czy_doskonala(liczba):
    suma_dzielnikow = 0
    for dzielnik in range(1, liczba):
        if liczba % dzielnik == 0:
            suma_dzielnikow += dzielnik

    return suma_dzielnikow == liczba


liczba = int(input("Podaj liczbe: "))
if czy_doskonala(liczba):
    print("Liczba jest doskonala")
else:
    print("Liczba nie jest doskonala")
