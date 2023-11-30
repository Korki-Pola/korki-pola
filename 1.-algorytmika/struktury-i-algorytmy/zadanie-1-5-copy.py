# iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego,

# Zlozonosc pamieciowa:     O(1)
# Zlozonosc obliczeniowa:   O(n)
def fib_iter(n, k):
    if n <= 0:
        return "Podaj liczbe wieksza od zera"

    if n == 1:
        return 0

    if n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b

    return b


wynik = fib_iter(4)
print(wynik)


# Zlozonosc pamieciowa:     O(2^n)
# Zlozonosc obliczeniowa:   O(2^n)
def fib_rek(n):
    if n <= 0:
        return "Podaj liczbe wieksza od zera"

    if n == 1:
        return 0

    if n == 2:
        return 1

    return fib_rek(n - 1) + fib_rek(n - 2)


wynik = fib_rek(4)
print(wynik)
