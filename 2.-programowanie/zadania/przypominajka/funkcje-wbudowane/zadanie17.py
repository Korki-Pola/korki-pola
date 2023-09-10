## Zadanie 17: Użycie `divmod` i `map`

# **Cel:** Dla listy liczb, znajdź iloraz i resztę z dzielenia przez 2.

numbers = [3, 7, 9, 12, 15]

results = list(map(lambda x: divmod(x,2), numbers))

for result in results:
    iloraz, reszta = result
    print(f'Iloraz i reszta z dzielenia liczby {numbers} przez 2 to: {iloraz}, {reszta}')
