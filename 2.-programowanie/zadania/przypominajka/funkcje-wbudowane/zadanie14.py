## Zadanie 14: Kombinacja funkcji `split` i `join`

# **Cel:** Zamień wszystkie spacje w stringu na myślniki.

text = "Ten przykladowy tekst ma 7 slow."

# UWAGA
# split() w formie bez argumentow dzieli tekst po wszystki white-characters czyli enter, spacja, tabulatura
# w tym zadaniu trzeba szukac kazdej spacji osobno wiec musimy uzyc split(" ")

new_text = "-".join(text.split(" "))
print(new_text)
