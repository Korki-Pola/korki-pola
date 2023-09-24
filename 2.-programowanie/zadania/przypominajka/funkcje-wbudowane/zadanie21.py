## Zadanie 21: Użycie funkcji `reduce` i `filter`

#**Cel:** Oblicz sumę liczb parzystych w liście.

with open("./zadanie21_output.txt", "w") as output_file:
    with open("./zadanie21_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            from functools import reduce
            liczby = range(0,11)
            suma_parzystych = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, liczby))
            print(suma_parzystych)
