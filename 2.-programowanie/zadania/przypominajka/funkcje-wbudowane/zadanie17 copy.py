## Zadanie 17: Użycie `divmod` i `map`

# **Cel:** Dla listy liczb, znajdź iloraz i resztę z dzielenia przez 2.

with open("./zadanie17_input.txt", "r") as dane:
    with open("./zadanie17_output.txt", "w") as wyniki:
        linijki = dane.readlines()

        for linijka in linijki:
            # 1. parsowanie danych z linijki
            # 1.1 pozbywamy sie enterow i [] z lewej i prawej strony
            sformatowana_linijka = linijka.strip('[]\n')
            # 1.2 rozdzielamy numerki w sformatowanej linijce
            # (separatorem jest ', ')
            # powstaje nam cos takiego '1, 2, 3' -> ['1', '2', '3']
            lista_linijka = sformatowana_linijka.split(', ')
            # 1.2 kazdy element z lista_linijka zamieniamy na int
            lista_int = list(map(lambda x: int(x), lista_linijka))

            # 2. wykonanie divmod na kazdej z liczb w uzyskanej liscie
            wynik = list(map(lambda x: (x, divmod(x, 2)), lista_int))

            # 3. wypisanie uzyskanych danych do pliku 'wyniki'
            print(wynik, file=wyniki)

