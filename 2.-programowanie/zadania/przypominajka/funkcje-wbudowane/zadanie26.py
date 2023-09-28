
## Zadanie 26: Kombinacja `divmod`, `map`, i `filter`

#**Cel:** Z listy liczb, znajdź te, które są podzielne przez 3 i 5, a następnie znajdź ich iloraz i resztę z dzielenia przez 3.

with open("./zadanie26_input.txt", "r") as input_file:
    with open("./zadanie26_output.txt", "w") as output_file:
        linijki = input_file.readlines()
        for linijka in linijki:
            numbers = list(range(0, 51))
            podzielne_num = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
            ilorazy_reszty = list(map(lambda x: divmod(x, 3), podzielne_num))
            print(podzielne_num and ilorazy_reszty, file=output_file)