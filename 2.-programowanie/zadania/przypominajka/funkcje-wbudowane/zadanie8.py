## Zadanie 8: Użycie funkcji `filter`

# **Cel:** Filtruj liczby parzyste z listy.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(number_list)
print(list(filter(lambda number: number % 2 == 0, number_list)))

return_list = []
for number in number_list:
    if number % 2 == 0:
        return_list.append(number)

print(return_list)