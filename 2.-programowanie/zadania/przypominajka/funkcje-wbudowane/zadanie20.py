## Zadanie 20: Użycie `join` i `map`

#**Cel:** Stwórz listę liczb i utwórz z niej string, w którym liczby są oddzielone przecinkami.

with open("./zadanie20_output.txt", "w") as output_file:
    with open("./zadanie20_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            liczby = [1,2,3,4,5]
            string_liczb = ", ".join(map(str,liczby))
            print(string_liczb)
