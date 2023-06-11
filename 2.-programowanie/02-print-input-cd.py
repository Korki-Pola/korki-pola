war_1 = input('Podaj pierwsza wartosc: ')
war_2 = input('Podaj druga wartosc: ')

kolumna_1_str = '1'
kolumna_2_str = '2'

len_war_1 = len(war_1)
war_2 *= 2
len_war_2 = len(war_2)

len_k_1 = len(kolumna_1_str)
len_k_2 = len(kolumna_2_str)

max_len_k_1 = max(len_war_1, len_k_1)
max_len_k_2 = max(len_war_2, len_k_2)

print('- ' * ((max_len_k_1 + max_len_k_2 + 3) // 2))
print(f'|{kolumna_1_str:^{max_len_k_1}}|{kolumna_2_str:^{max_len_k_2}}|')
print('- ' * ((max_len_k_1 + max_len_k_2 + 3) // 2))
print(f'|{war_1:^{max_len_k_1}}|{war_2:^{max_len_k_2}}|')
print('- ' * ((max_len_k_1 + max_len_k_2 + 3) // 2))
