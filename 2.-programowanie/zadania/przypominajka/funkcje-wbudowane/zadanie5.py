## Zadanie 5: Użycie funkcji `open` do odczytu pliku

#**Cel:** Odczytaj plik tekstowy i wydrukuj jego zawartość.

with open('./zadanie5-input.txt', 'r') as plik:
    zawartosc = plik.read()
    print(zawartosc)

#trzeba pobrac z jakiegos pliku