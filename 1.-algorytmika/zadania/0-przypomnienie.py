# typy danych
# proste typy
wartosc_calkowita: int = 13
wartosc_zmiennoprzecinkowa: float = 13.4
wartosc_logiczna: bool = True and 3 == 4    # wartosc bedzie False

# zlozone typy
# str
wartosc_tekstowa: str = 'jestem stringiem'

# krotka - raczej nie bedziesz ich tworzyc (dziala jak lista ale jest TYLKO DO ODCZYTU)
krotka: tuple = (0, 1, 'sfljasdlf', [], {})

# listy to zbior elementow jeden po drugim, kazdy ma swoj indeks (od 0 w gore)
lista_int: list[int] = [0, 0, 123, 324523, -132]
lista: list = [13, 0.123, 'fdsf', [], [32, 323, 54], {'foo': 'bar'}]
lista[1]    # 0.123
lista[4]    # [32, 323, 54]
lista[4][1] # 323
lista[5]    # {'foo': 'bar'}
lista[5]['foo']  # 'bar'
lista[0] = 10   # [10, 0.123, 'fdsf', [], [32, 323, 54], {'foo': 'bar'}]

# slowniki
slownik: dict = {
    'foo': 4,
    'bar': 15.3,
    'baz': 'bac',
    13: [13, 343, 15],
    -1: {
        'a': 'a',
        'b': 'b',
    },
    14.5: True,
}

slownik['foo'] = 5  # nadpisze wartosc klucza foo lub stworzy nowy klucz i da mu wartosc 5
slownik['foo']  # 4
slownik[13]     # [13, 343, 15]
slownik[13][0]  # 13

##################################################

# Funkcje skojarzone z typami zlozonymi
# str
# split
'foo bar\nbaz'.split()  # ['foo', 'bar', 'baz']
'a,2,3 , 4'.split(',')  # ['a', '2', '3 ', ' 4']
# strip
'    asdfsdaf    '.strip()      # 'asdfsdaf'
'\n \n  asdfkj \nsdf'.strip()   # 'asdfkj \nsdf'
'foofoofoofoobazbarbazfoofoo'.strip('foo')  # 'bazbarbaz'
'foofoofoofoobazbarbazfoofoo'.lstrip('foo')     # 'bazbarbazfoofoo'
'foofoofoofoobazbarbazfoofoo'.rstrip('foo')     # 'foofoofoofoobazbarbaz'

# list
[1, 2, 3, 4].append(5)  # [1, 2, 3, 4, 5]
[1, 2, 3, 4].clear()    # []
[1, 2, 3, 4].pop()      # 4
[1, 2, 3, 4].insert(0, 10)   # [10, 2, 3, 4]

lista = [1, 2, 3, 4]
lista.reverse()  # [4, 3, 2, 1] !!UWAGA!! operacja ma miejsce w miejscu (nie jest tworzona kopia, czyli lista zostala odwrocona)
lista = [1, 2, 3, 4]
list(reversed(lista))    # [1, 2, 3, 4] -> [4, 3, 2, 1] (nie lista zostaje zwrocona a jej odwrocona kopia)

# dict
slownik = {'foo': 1, 'bar': 2}
slownik.clear()     # slownik: {}
slownik.pop('foo')  # slownik: {'bar': 2}, zwraca: 1
slownik.get('foo')  # slownik: {'foo': 1, 'bar': 2}, zwraca: 1
slownik.keys()      # slownik: {'foo': 1, 'bar': 2}, zwraca: ['foo', 'bar']
slownik.values()    # slownik: {'foo': 1, 'bar': 2}, zwraca: [1, 2]
slownik.items()     # slownik: {'foo': 1, 'bar': 2}, zwraca: [('foo', 1), ('bar', 2)]

##########################

# Keywordy i specjalne funckje
warunek_0 = None
warunek_1 = None

if warunek_0:
    pass
elif warunek_1:
    pass
else:
    pass


while warunek_0:
    pass

for x in lista:
    pass


# FUNCKJE
# definicja funkcji
def najprostsza_funkcja() -> None:
    return

# uzycie funckji
najprostsza_funkcja()

def suma(a: int, b: int) -> int:
    return a + b

wynik_dodawania_0 = suma(3, 5)
wynik_dodawania_1 = suma(3, 10)
wynik_dodawania_2 = suma(3, 4)
wynik_dodawania_3 = suma(123123, 123)
wynik_dodawania_4 = suma(3, 5)
