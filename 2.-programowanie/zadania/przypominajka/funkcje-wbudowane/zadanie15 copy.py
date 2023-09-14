## Zadanie 15: Użycie funkcji `sum` z `map`

# **Cel:** Oblicz sumę kwadratów liczb w liście.

with open("./zadanie15_output.txt", "w") as output_file:
    with open("./zadanie15_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            # dokoncz parsowanie danych wejsciowych 
            # zrob cos z wartoscia 'linijka' zeby otrzymac poprawna wartosc 'lista_numerow'
            lista_numerow = 

            # wykonanie algorytmu
            sum_of_squares = sum(map(lambda x: x ** 2, lista_numerow))
            print(sum_of_squares, file=output_file)
