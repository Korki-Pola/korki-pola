## Zadanie 6: Użycie `map` i `list`

# **Cel:** Utwórz listę z pięcioma liczbami i podnieś każdą z nich do kwadratu.

def mapping_function(number: int):
    return number ** 2

# lambda_mapping_function = lambda number: number ** 2

number_list = [1, 2, 3, 4, 5]
print(list(map(lambda number: number ** 2, number_list)))
print(list(map(mapping_function, number_list)))