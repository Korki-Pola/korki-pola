ciag_znakow: str = 'asdlfjlasdjflk'

# pierwszy sposob
lista_znakow_1 = list(reversed(ciag_znakow))
print(''.join(lista_znakow_1))

# drugi sposob
lista_znakow_2 = list(ciag_znakow)
lista_znakow_2.reverse()
print(''.join(lista_znakow_2))

# trzeci sposob
dlugosc_ciagu_znakow = len(ciag_znakow)
lista = []
for _ in range(dlugosc_ciagu_znakow):
    lista.append(None)

for i in range(dlugosc_ciagu_znakow):
    znak = ciag_znakow[i]
    nowy_indeks = dlugosc_ciagu_znakow - i - 1
    lista[nowy_indeks] = znak

print(''.join(lista))
