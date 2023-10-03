## Zadanie 29: Kombinacja `open`, `read`/`readlines`, `split`, `map`, `filter`, i `reduce`

#**Cel:** Odczytaj plik zawierający liczby oddzielone przecinkami, wybierz liczby parzyste, podnieś je do kwadratu i oblicz ich sumę.

with open("./zadanie29_input.txt", "r") as input_file:
    with open("./zadanie29_input.txt", "w") as output_file:
        linijki = input_file.readlines()
        for linijka in linijki:
            liczby = input_file.read().split(',')
            liczby_parzyste = list(filter(lambda x: int(x) % 2 == 0, liczby))
            liczby_kwadratowe = list(map(lambda x: int(x) ** 2, liczby_parzyste))
            suma = sum(liczby_kwadratowe)
            print(sum, file=output_file)
