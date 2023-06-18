lista = [1, 2, 3, 4, 5]
odwrocona_lista_1 = lista[::-1]

# probuj nie korzystac z metody .reverse()
odwrocona_lista_2 = []
for el in lista:
    odwrocona_lista_2.append(el)
odwrocona_lista_2.reverse()

odwrocona_lista_3 = list(reversed(lista))

print(odwrocona_lista_1)
print(odwrocona_lista_2)
print(odwrocona_lista_3)
