# **FizzBuzz**: Licz od 1 do 100, ale dla wielokrotności 3, zamiast liczby, 
# wydrukuj "Fizz", dla wielokrotności 5 wydrukuj "Buzz", a dla liczb, 
# które są wielokrotnościami zarówno 3, jak i 5, wydrukuj "FizzBuzz".

# dodatkowe warunki:
# - wypisz Mizz jak podzielna przez 7
# - wypisz Gizz jak podzielna przez 12

for liczba in range(1, 16):
    czy_wypisac_liczbe = True
    if liczba % 3 == 0:
        print("Fizz", end='')
        czy_wypisac_liczbe = False

    if liczba % 5 == 0:
        print("Buzz", end='')
        czy_wypisac_liczbe = False

    if czy_wypisac_liczbe:
        print(liczba)
    else:
        print()
