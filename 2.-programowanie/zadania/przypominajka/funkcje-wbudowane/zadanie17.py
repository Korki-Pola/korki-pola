## Zadanie 17: Użycie `divmod` i `map`

# **Cel:** Dla listy liczb, znajdź iloraz i resztę z dzielenia przez 2.

def mapuj_divmod(x):
    (iloraz, reszta) = divmod(x, 2)
    return (x, iloraz, reszta)


numbers = [3, 7, 9, 12, 15]

# okej ale brakuje info o numerze na kotrym zostal wykonany divmod (do pozniejszego uzycia w for loopie)
# results = list(map(lambda x: divmod(x, 2), numbers))

# pomysla okej ale wykonaniue chujowe
# results = list(map(lambda x: (x, divmod(x, 2)[0], divmod(x, 2)[1]), numbers))

# zgrabniejsze od tego na gorze
with open("./zadanie17_output.txt", "w") as output_file:
    with open("./zadanie17_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            lista_numerow_str = linijka.strip('[]\n').split(', ')
            lista_numerow = list(map(lambda x: int(x), lista_numerow_str))

            results = list(map(mapuj_divmod, numbers))

            for result in results:
                (number, iloraz, reszta) = result
                print(f'Iloraz i reszta z dzielenia liczby {number} przez 2 to: {iloraz}, {reszta}', file=output_file)
