## Zadanie 13: Kombinacja funkcji `map` i `filter`

# **Cel:** Podnieś do kwadratu tylko liczby parzyste w liście.

numbers = [1, 2, 3, 4, 5, 6]

squared_numbers = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

print(squared_numbers)
