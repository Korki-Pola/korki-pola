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


def is_prime(possible_prime: int | None) -> bool:
    if possible_prime is None or possible_prime < 2:
        return False

    upper_bound = possible_prime ** 1/2
    values = [2, 3]
    values.extend([x for x in range(4, math.ceil(upper_bound + 1))])
    for value in values:
        if possible_prime % value == 0:
            return False

    return True


def get_primes(upper_bound: int) -> list[int]:
    values = [2, 3]
    values.extend([x for x in range(4, math.ceil(upper_bound + 1))])

    for index in range(len(values)):
        value = values[index]

        if is_prime(value):
            for j in range(index + value, len(values), value):
                values[j] = None

    filtered_values = []
    for v in values:
        if v is not None:
            filtered_values.append(v)

    return filtered_values


def get_prime_factors(n: int) -> list[int]:
    primes = get_primes(n ** 1/2)
    prime_factors = []
    index = 0
    while n != 1:
        prime = primes[index]
        if n % prime == 0:
            prime_factors.append(prime)
            n = n // prime
        else:
            index += 1

    return prime_factors


print(get_prime_factors(4))         # [2, 2]
print(get_prime_factors(3))         # [3]
print(get_prime_factors(1000))      # [2, 2, 2, 5, 5, 5]
