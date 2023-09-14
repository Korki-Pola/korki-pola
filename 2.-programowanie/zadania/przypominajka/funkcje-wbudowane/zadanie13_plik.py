# Zadanie 13: Kombinacja funkcji `map` i `filter`
# dla kazdej linijki z pliku zadanie13_input.txt wykonaj
# ponizszy cel i zapis go w pliku zadanie13_output.txt

# **Cel:** Podnieś do kwadratu tylko liczby parzyste w liście.

# TODO: zadanie 14 do 17 zrob dokladnie to samo - potworze ci pliki 'input'

with open("./zadanie13_output.txt", "w") as output_file:
    with open("./zadanie13_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            # przetwarzanie inputu (tzw. parsowanie)
            lista_numerow_str = linijka.strip('[]\n').split(', ')
            lista_numerow = list(map(lambda x: int(x), lista_numerow_str))

            # wykonanie algorytmu na przetworzonych (sparsowanych) danych
            lista_parzystych_num = list(filter(lambda x: x % 2 == 0, lista_numerow))
            lista_kwadratow = list(map(lambda x: x ** 2, lista_parzystych_num))
            print(lista_kwadratow, file=output_file)
