# WHILE
wartosc_1 = int(input("Podaj wartosc_1: "))
wartosc_2 = int(input("Podaj wartosc_2: "))

while wartosc_1 < 10 and wartosc_1 < wartosc_2:
    print(wartosc_1)
    wartosc_1 += 1

# WITH i slowo AS
# czytanie z pliku
with open('dupa.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        print(line.strip())


# wczytywanie do pliku
with open('result.txt', 'w') as f:
    # file.write("Hello World")
    # file.write("FizzBuzz")

    for _ in range(0, 6):
        print("Hello", "World", file=f, sep='-', end=' dupa\n')

# TRY - EXCEPT
try:
    num_1 = 1
    num_2 = 0
    # wyrzuca (throws) ZeroDivisionError
    print(num_1 / num_2)

    lista = [0, 1]
    # wyrzuca (throws) IndexError
    print(lista[12])
except ZeroDivisionError as zeroDivisionErrorMessage:
    print(zeroDivisionErrorMessage)
except IndexError as indexErrorMessage:
    print(indexErrorMessage)

try:
    num_3 = int(input("Podaj wartosc calkowita: "))
except ValueError as valueErrorMessage:
    num_3 = 0
    print("Nie umiesz czytac debilu")
print(num_3)


# SLOWNIKI
dict_1 = {
    'dafdf': "sdafkljsdfl",
    2343: 382179382,
    'sdlkfj': [1, 2, 3, 3, 4],
    'slownik': {
        'sdjflkkjlakdfjalskd': 12318273
    }
}

print(dict_1.get('dafdf'))
print(dict_1.get(2343))
print(dict_1.get('sdlkfj'))
print(dict_1.get('slownik'))

dict_1.update({"color": 'red'})
print(dict_1)
dict_1['imie'] = 'Pola'
print(dict_1)

keys_of_dict_1 = list(dict_1.keys())
values_of_dict_1 = list(dict_1.values())

print(keys_of_dict_1, values_of_dict_1, sep='\n')


# FUNKCJE
# tworzenie funkcji
def funkcja() -> None:
    pass


# KLASY
# tworzenie klas
class Klasa:
    def __init__(self) -> None:
        pass
