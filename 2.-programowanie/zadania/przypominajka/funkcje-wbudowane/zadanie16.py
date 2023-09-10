## Zadanie 16: Użycie `input` i `int`
#
# **Cel:** Pobierz dwie liczby od użytkownika i oblicz ich sumę.
try:
    liczba_1 = int(input("Podaj pierwsza liczbe calkowita: "))
    liczba_2 = int(input("Podaj druga liczbe calkowita: "))

    suma = liczba_1 + liczba_2

    print(f'Suma tych liczb wynosi: {suma}')

except ValueError:
    print("To nie liczba idioto.")

