## Zadanie 28: Kombinacja `open`, `filter`, i `write`

#**Cel:** Odczytaj plik, wybierz linie zawierające słowo "Python" i zapisz je do nowego pliku.

with open("./zadanie28_input.txt", "r") as input_file:
    with open("./zadanie28_input.txt", "w") as output_file:
        linijki = input_file.readlines()
        for linijka in linijki:
            linie_python = filter(lambda linia: 'Python' in linijka, input_file)
            print(linie_python, file=output_file)
