## Zadanie 14: Kombinacja funkcji `split` i `join`

# **Cel:** Zamień wszystkie spacje w stringu na myślniki.

with open("./zadanie14_output.txt", "w") as output_file:
    with open("./zadanie14_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            # dokoncz parsowanie danych wejsciowych
            # zrob cos z wartoscia 'linijka' zeby otrzymac poprawna wartosc 'text'
            text = 

            # UWAGA
            # split() w formie bez argumentow dzieli tekst po wszystki white-characters czyli enter, spacja, tabulatura
            # w tym zadaniu trzeba szukac kazdej spacji osobno wiec musimy uzyc split(" ")

            new_text = "-".join(text.split(" "))
            print(new_text, file=output_file)