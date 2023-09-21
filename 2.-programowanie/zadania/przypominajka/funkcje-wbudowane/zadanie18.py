# Zadanie 18: Funkcje `open`, `read`/`readlines` i `split`

# **Cel:** Odczytaj plik, podziel go na linie i zlicz ich ilość.

with open("./zadanie18_input.txt", "r") as input:
    print(len(input.readlines()))
