## Zadanie 16 - plik: Użycie `input` i `int`
#
# **Cel:** Pobierz liczby z pliku i oblicz ich sumę.

with open("./zadanie16_output.txt", "w") as output_file:
    with open("./zadanie16_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            # dokoncz parsowanie danych wejsciowych
            # zrob cos z wartoscia 'linijka' zeby otrzymac poprawna wartosc 'liczby'
            liczby_str = linijka.strip('\n').split(', ')
            liczby = list(map(lambda x: int(x), liczby_str))

            # wykonanie algorytmu
            suma = sum(liczby)
            print(f'Suma tych liczb wynosi: {suma}', file=output_file)
