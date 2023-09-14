## Zadanie 16: Użycie `input` i `int`
#
# **Cel:** Pobierz dwie liczby od użytkownika i oblicz ich sumę.

with open("./zadanie16_output.txt", "w") as output_file:
    with open("./zadanie16_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            lista_numerow_str = linijka.strip('[]\n').split(', ')
            lista_numerow = list(map(lambda x: int(x), lista_numerow_str))

            try:
                liczba_1 = 4 #int(input("Podaj pierwsza liczbe calkowita: "))
                liczba_2 = 8 #int(input("Podaj druga liczbe calkowita: "))

                suma = liczba_1 + liczba_2

                print(f'Suma tych liczb wynosi: {suma}', file=output_file)

            except ValueError:
                print("To nie liczba idioto.", file=output_file)
