# ZADANI DOMOWE
# Napisac funkcje zwracajaca czynniki pierwsze danej liczby N

# 1. dostajemy liczbe N ktorej czynniki mamy znalezc
#
# 2. budujemy liste liczb pierwszych od 2 do sqrt(N)
# (wlacznie) (np. N = 16 to lista -> [2, 3], N = 1024 lista -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
#
# 3. przedchodzimy przez liste liczb pierwszych i jezeli dana liczba P
# (liczba z listy liczb pierwszych) dzieli N to zapisujemy ja jaka czynnik pierwszy,
# zapisujemy N = N // P i dzielimy N przez P jeszcze raz
# (i tak w kolko poki spelnione) - jezeli nie dzieli to przechodzimy do nastepnej liczby P
# Warunek konca: n == 1

import math


def is_prime(possible_prime: int) -> bool:
    pass

# uzywa is_prime
def get_primes(upper_bound: int) -> list[int]:
    pass


def get_prime_factors(n: int) -> list[int]:
    primes = get_primes(math.ceil(n ** 1/2))
    pass
