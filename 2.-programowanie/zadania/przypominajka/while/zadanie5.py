# Suma Liczb: Używając pętli while, zsumuj wszystkie liczby
# miedzy 1 a 20 i wypisz ich sume
poczatkowa_liczba = 0
koncowa_liczba = 20
licznik = poczatkowa_liczba
while licznik < koncowa_liczba:
    nowy_licznik = licznik + 1
    print(licznik)
    licznik = nowy_licznik
suma = 0
liczba = 1

while liczba <= 20:
    suma += liczba
    liczba += 1

print("Suma liczb od 1 do 20 wynosi: "f'{suma}')