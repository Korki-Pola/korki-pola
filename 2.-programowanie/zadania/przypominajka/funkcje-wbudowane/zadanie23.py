## Zadanie 23: Użycie funkcji `open`, `write` i `join`

# **Cel:** Zapisz listę liczb do pliku, oddzielając je przecinkami.

with open("./zadanie23_output.txt", "w") as output_file:
    liczby = list(range(-10, 10))

    liczby_str = ','.join(list(map(str, liczby)))

    print(liczby_str, file=output_file)
