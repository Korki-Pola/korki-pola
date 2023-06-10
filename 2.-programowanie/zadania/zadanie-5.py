value_1 = input('Podaj pierwszą wartość: ')
value_2 = input('Podaj druga wartość: ')
value_3 = input('Podaj trzecią wartość: ')
value_4 = input('Podaj czwartą wartość: ')

len_value_1 = len(value_1)
len_value_2 = len(value_2)
len_value_3 = len(value_3)
len_value_4 = len(value_4)

max_len_val = max(len_value_1, len_value_2, len_value_3, len_value_4)

print(f'Najdłuższa wartość to:{max_len_val}')