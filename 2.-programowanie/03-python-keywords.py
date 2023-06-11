# if / if else / if elif else/ itd... - warunki (sprawdzenie jednokrotne)

zmienna = float(input("Podaj wartosc zmiennoprzecinkowa: "))

warunek1 = zmienna < 0
warunek2 = zmienna == 0

if warunek1:
    # cialo if'a - czyli poprostu kod
    print(f'Liczba {zmienna} jest mniejsza od 0')
elif warunek2:
    # cialo elif'a - czyli poprostu kod
    print(f'Liczba {zmienna} jest rowna 0')
else:
    # cialo else'a - czyli poprostu kod
    print(f'Liczba {zmienna} jest wieksza od 0')

# for - iteracja

# lista
lista = [1, 2, 3, 4, 5, 6]

print('lista')
for element in lista:
    print(element)

print('odwrocona lista')
for element in reversed(lista):
    print(element)

print('range')
for i in range(1, 7):
    print(i)

print('odwrocony range #1')
for i in range(6, 0, -1):
    print(i)

print('odwrocony range #2')
for i in reversed(range(1, 7)):
    print(i)

print('range od 0 do 6 co 2')
for i in range(1, 7, 2):
    print(i)

print('range od -10 do 13 co 3')
for i in range(-10, 14, 3):
    print(i)

print('range od 13 do -10 co -3')
for i in range(13, -11, -3):
    print(i)

# szybko o listach
print('szybko o listach')
lista = [1, 2, 3, 4, 5, 6]

print('odczytywanie / manipulacja wartosciami listy')
print(lista[0])
print(lista[5])
print(lista[-4])
print(lista[0:2])
print(lista[5:3:-1])
print(lista[0:5:2])
print(lista[4:-1:-1])
print(lista[4:0:-1])
print(lista[4::-1])
print(lista[:3:-1])
print(lista[:3:1])
print(lista[::-1])
print(lista[::-2])

# dlugosc listy
print('dlugosc listy')
print(len(lista))

# dodawanie wartosci do listy
print('dodawanie wartosci do listy')
lista.append(7)
print(lista)

# usuwanie wartosci z listy
print('usuwanie wartosci z listy')
lista.remove(7)
print(lista)

# usuwanie ostatniej wartosci z listy
print('usuwanie ostatniej wartosci z listy')
lista.pop()
print(lista)

# usuwanie wartosci o danym index-ie z listy
print('usuwanie wartosci o danym index-ie z listy')
lista.pop(0)
print(lista)
