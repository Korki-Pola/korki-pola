## Zadanie 12: Użycie funkcji `reduce`

# **Cel:** Pomnóż wszystkie elementy w liście.


from functools import reduce

number_list = [1, 2, 3, 4, 5]

print(sum(number_list))
print(reduce(lambda accumulator, number: accumulator + number, number_list, 0))




