## Zadanie 15: Użycie funkcji `sum` z `map`

# **Cel:** Oblicz sumę kwadratów liczb w liście.

with open("./zadanie15_output.txt", "w") as output_file:
    with open("./zadanie15_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            # parsowanie danych wejsciowych
            lista_numerow_str = linijka.strip('[]\n').split(', ')
            lista_numerow = list(map(lambda x: int(x), lista_numerow_str))

            # wykonanie algorytmu
            sum_of_squares = sum(map(lambda x: x ** 2, lista_numerow))
            print(sum_of_squares, file=output_file)
