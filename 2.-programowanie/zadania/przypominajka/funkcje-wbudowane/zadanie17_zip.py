## Zadanie 17: Użycie `divmod` i `map`

# **Cel:** Dla listy liczb, znajdź iloraz i resztę z dzielenia przez 2.

numbers = [3, 7, 9, 12, 15]

results = list(map(lambda x: divmod(x, 2), numbers))

for (result, number) in zip(results, numbers):
    (iloraz, reszta) = result
    print(f'Iloraz i reszta z dzielenia liczby {number} przez 2 to: {iloraz}, {reszta}')



# jak dziala ???zip(lista_a, lista_b) =>
lista_a = [0, 1, 2, 3, 4]
lista_b = ['a', 'b', 'c', 'd', 'e']

lista_z_zipa = []
for index in range(0, 5):
    lista_z_zipa.append((lista_a[index], lista_b[index]))

# lista_z_zipa => [(0, 'a'), (1, 'b'), ...itd]