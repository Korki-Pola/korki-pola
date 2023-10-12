## Zadanie 27: Użycie funkcji `split`, `filter`, i `join`

# **Cel:** Pobierz od użytkownika/Pobierz z pliku zdanie i wyświetl tylko te
# słowa, które mają więcej niż 4 znaki.

with open('./zadanie27_input.txt', 'r') as input_file:
    with open('./zadanie27_output.txt', 'w') as output_file:
        linijki = input_file.readlines()
        for linijka in linijki:
            # linijka jest zdaniem - przepisujemy do innej
            # zmiennej w celu wyjasnienia dzialania kodu
            zdanie = linijka
            slowa = zdanie.split()
            slowa_dluzsze_niz_4_znaki = list(filter(lambda x: len(x) > 4, slowa))

            for slowo in slowa_dluzsze_niz_4_znaki:
                print(slowo, file=output_file, end=', ')
            print(file=output_file)
