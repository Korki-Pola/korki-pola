## Zadanie 13: Kombinacja funkcji `map` i `filter`

# **Cel:** Podnieś do kwadratu tylko liczby parzyste w liście.

start_num = -5
end_num = 15

numbers = map(lambda x: x * 0.5, [x for x in range(start_num, end_num + 1)])    # sposb na sprawdzenie czy liczby ulamkowe tez dzialaja

# [x / 2 for x in range(start_num, end_num + 1)] odpowiednik na dole:
# 
# lista = []
# for x in range(start_num, end_num + 1):
#     lista.append(x / 2)

filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(filtered_numbers)

squared_numbers = list(map(lambda x: x ** 2, filtered_numbers))

print(squared_numbers)
