value_1 = input('Podaj pierwszą wartość: ')
value_2 = input('Podaj druga wartość: ')
value_3 = input('Podaj trzecią wartość: ')
value_4 = input('Podaj czwartą wartość: ')

longest_value = max(value_1, value_2, value_3, value_4, key=len)
lenght = len(longest_value)

print(f'Najdłuższa wartość to {longest_value} i ma długość {lenght}.')
