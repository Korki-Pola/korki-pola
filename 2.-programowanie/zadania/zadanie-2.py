imie = input("Podaj swoje imie: ")
nazwisko = input("Podaj swoje nazwisko: ")
drugie_imie = input("Podaj swoje drugie imie: ")

kolumna_1_str = 'IMIE'
kolumna_2_str = 'NAZWISKO'
kolumna_3_str = 'DRUGIE IMIE'

len_imie = len(imie)
len_nazwisko = len(nazwisko)
len_drugie_imie = len(drugie_imie)

len_k_1_str = len(kolumna_1_str)
len_k_2_str = len(kolumna_2_str)
len_k_3_str = len(kolumna_3_str)

max_len_k_1 = max(len_imie, len_k_1_str)
max_len_k_2 = max(len_nazwisko, len_k_2_str)
max_len_k_3 = max(len_drugie_imie, len_k_3_str)

len_k_1 = max_len_k_1 + 2
len_k_2 = max_len_k_2 + 2
len_k_3 = max_len_k_3 + 2

len_minuses = len_k_1 + len_k_2 + len_k_3 + 4

print('-' * len_minuses)
print(f'|{kolumna_1_str:^{len_k_1}}|{kolumna_2_str:^{len_k_2}}|{kolumna_3_str:^{len_k_3}}|')
print('-' * len_minuses)
print(f'|{imie:^{len_k_1}}|{nazwisko:^{len_k_2}}|{drugie_imie:^{len_k_3}}|')
print('-' * len_minuses)
