## Zadanie 28: Kombinacja `open`, `filter`, i `write`

#**Cel:** Odczytaj plik, wybierz linie zawierające słowo "Python" i
# zapisz je do nowego pliku.

with open("./zadanie28_input.txt", "r") as input_file:
    with open("./zadanie28_output.txt", "w") as output_file:
        linijki = input_file.readlines()

        # Sposob nr 1
        # x to linijka z listy linijki w kontekscie filter
        linijki_ze_slowem_python = list(filter(lambda x: 'Python' in x, linijki))
        for linijka in linijki_ze_slowem_python:
            print(linijka.strip(), file=output_file)

        # Sposob nr 2
        # for linijka in linijki:
        #     if 'Python' in linijka:
        #         print(linijka, file=output_file)
