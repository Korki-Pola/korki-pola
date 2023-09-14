## Zadanie 14: Kombinacja funkcji `split` i `join`

# **Cel:** Zamień wszystkie spacje w stringu na myślniki.

with open("./zadanie14_output.txt", "w") as output_file:
    with open("./zadanie14_input.txt", "r") as input_file:
        for linijka in input_file.readlines():
            lista_numerow_str = linijka.strip('[]\n').split(', ')
            #lista_numerow = list(map(lambda x: int(x), lista_numerow_str))

            text = "Ten przykladowy tekst ma 7 slow."

# UWAGA
# split() w formie bez argumentow dzieli tekst po wszystki white-characters czyli enter, spacja, tabulatura
# w tym zadaniu trzeba szukac kazdej spacji osobno wiec musimy uzyc split(" ")

            new_text = "-".join(text.split(" "))
            print(new_text, file=output_file)