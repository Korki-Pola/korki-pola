# Zadanie 22: Kombinacja `input`, `split` i `map`
# **Cel:** Pobierz od użytkownika/Pobierz z pliku listę liczb oddzielonych przecinkami i oblicz ich sumę.

with open("./zadanie22_input.txt", "r") as input_file:
    with open("./zadanie22_output.txt", "w") as output_file:
        linijki = input_file.readlines()
        for linijka in linijki:
            liczby = list(map(int, linijka.strip('\n').split(",")))

            suma = sum(liczby)
            print(suma, file=output_file)
