## Zadanie 15: Użycie funkcji `sum` z `map`

# **Cel:** Oblicz sumę kwadratów liczb w liście.

with open("./zadanie15_output.txt", "w") as output_file:
    with open("./zadanie15_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            lista_numerow_str = linijka.strip('[]\n').split(', ')
            lista_numerow = list(map(lambda x: int(x), lista_numerow_str))

            numbers = [1, 2, 3, 4, 5]

            sum_of_squares = sum(map(lambda x: x ** 2, numbers))

            print(sum_of_squares, file=output_file)
