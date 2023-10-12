## Zadanie 29: Kombinacja `open`, `read`/`readlines`, `split`, `map`, `filter`, i `reduce`

#**Cel:** Odczytaj plik zawierający liczby oddzielone przecinkami, dla kazdej linijki
# wybierz liczby parzyste, podnieś je do kwadratu i oblicz ich sumę.

with open("./zadanie29_input.txt", "r") as input_file:
    with open("./zadanie29_output.txt", "w") as output_file:
        linijki = input_file.readlines()
        for linijka in linijki:
            stringi_przedstawiajace_liczby = linijka.strip().split(',')

            liczby = []
            for liczba_str in stringi_przedstawiajace_liczby:
                liczba = int(liczba_str)

                if liczba % 2 == 0:
                    liczby.append(liczba)

            liczby_do_kwadratu = []
            for liczba in liczby:
                liczba_2 = liczba ** 2
                liczby_do_kwadratu.append(liczba_2)

            suma_liczb = sum(liczby_do_kwadratu)
            print(suma_liczb, file=output_file)








