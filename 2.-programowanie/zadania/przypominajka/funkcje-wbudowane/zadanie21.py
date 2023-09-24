## Zadanie 21: Użycie funkcji `reduce` i `filter`

#**Cel:** Oblicz sumę liczb parzystych w liście.

from functools import reduce


with open("./zadanie21_output.txt", "w") as output_file:
    with open("./zadanie21_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            # linijka (jest na poczatku) => '[12, 45, 78, 9, 63]\n' to jest str
            # '12, 45, 78, 9, 63' => ['12', '45', '78', '9', '63']
            # int('12') => 12
            # liczby (czym maja byc) => [12, 45, 78, 9, 63] to jest list[int]
            liczby = list(map(int, linijka.strip("[]\n").split(", ")))

            suma_parzystych = reduce(lambda accumulator, y: accumulator + y, filter(lambda x: x % 2 == 0, liczby), 0)
            print(suma_parzystych, file=output_file)
