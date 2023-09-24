## Zadanie 20: Użycie `strip` i `replace`

# **Cel:** Stwórz listę liczb i utwórz z niej string, w którym liczby są oddzielone przecinkami.

with open("./zadanie20_output.txt", "w") as output_file:
    with open("./zadanie20_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            zmodyfikowana_linijka = linijka.strip("[]\n").replace(" ", "")
            print(zmodyfikowana_linijka, file=output_file)
