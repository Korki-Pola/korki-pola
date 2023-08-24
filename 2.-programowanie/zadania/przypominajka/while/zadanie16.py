# **FizzBuzz**: Licz od 1 do 100, ale dla wielokrotności 3, zamiast liczby, 
# wydrukuj "Fizz", dla wielokrotności 5 wydrukuj "Buzz", a dla liczb, 
# które są wielokrotnościami zarówno 3, jak i 5, wydrukuj "FizzBuzz".

# dodatkowe warunki:
# - wypisz Mizz jak podzielna przez 7
# - wypisz Gizz jak podzielna przez 12


def sprawdz_czy_wypisac(element, dzielnik, slowo) -> bool:
    if element % dzielnik == 0:
        print(slowo, end='')
        return True
    else:
        return False


zestaw_regul = [(3, "Fizz"), (5, "Buzz"), (7, "Mizz"), (12, "Gizz")]


for element in range(1, 101):
    doszlo_do_ifa = False

    for regula in zestaw_regul:
        wynik = sprawdz_czy_wypisac(element, regula[0], regula[1])
        doszlo_do_ifa = wynik or doszlo_do_ifa

    if not doszlo_do_ifa:
        print(element)
    else:
        print()

