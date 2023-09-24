## Zadanie 27: Użycie funkcji `split`, `filter`, i `join`

# **Cel:** Pobierz od użytkownika/Pobierz z pliku zdanie i wyświetl tylko te
# słowa, które mają więcej niż 4 znaki.

with open('./zadanie27_input.txt', 'r') as input_file:
    linijki = input_file.readlines()
    for linijka in linijki:
        slowa = linijka.strip("\n").split(" ")

        slowa_dluzsze_niz_4_znaki = list(filter(lambda x: len(x) > 4, slowa))

        print(slowa_dluzsze_niz_4_znaki)
