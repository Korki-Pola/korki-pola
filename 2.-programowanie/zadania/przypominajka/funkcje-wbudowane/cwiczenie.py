# dwa sposoby na importowanie rzeczy
# 1.
from przykladowy_modul import wypisz_dupa, wypisz_cycki
# 2.
# import przykladowy_modul

from functools import reduce

# uzycie zaimportowanych rzeczy
# 1.
wypisz_dupa()
wypisz_cycki()
# 2.
# przykladowy_modul.wypisz_dupa()
# przykladowy_modul.wypisz_cycki()

# TODO: Praca domowa:
# W pliku './cwiczenia.py' pobaw sie funkcjami reduce, map, filter (reduce, map i filter dzialaja na listach)
# oraz split i join (split i join dzialaja na stringach). lorem ipsum
# Pamietaj o zaimportowaniu funkcji reduce.
# Pobaw sie rowniez funkcja open (wraz ze slowami with i as).

user_input = int(input('Podaj wartosc dla ktorej obliczymy silnie: '))

if user_input == 0:
    print(f'{user_input}! = {1}')
else:
    lista = [x + 1 for x in range(0, user_input)]
    silnia = reduce(lambda accumulator, numer: accumulator * numer, lista, 1)

    if user_input < 0:
        print(f'Brak silni dla wartosci {user_input}')
    else:
        print(f'{user_input}! = {silnia}')


ujemno_dodatnia_lista = [x - 3 for x in range(10)]
nowa_ujemno_dodatnia_lista = list(filter(lambda numer: numer > 0, ujemno_dodatnia_lista))
print(f'nowa_ujemno_dodatnia_lista: {nowa_ujemno_dodatnia_lista}')
print(reduce(lambda accumulator, number: accumulator * number, ujemno_dodatnia_lista, 1))


dodatnia_lista = [x for x in range(10)]
nowa_dodatnia_lista = list(map(lambda numer: numer + 1, dodatnia_lista))
print(f'nowa_dodatnia_lista: {nowa_dodatnia_lista}')
print(reduce(lambda accumulator, number: accumulator * number, nowa_dodatnia_lista, 1))
