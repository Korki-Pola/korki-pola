#iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego,

def fib_iter(n):
    if n <= 0:
        return "Podaj liczbe wieksza od zera"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0,1
        for _ in range(2, n):
            a,b = b,a + b
        return b


wynik = fib_iter(6)
print(wynik)


def fib_rek(n):
    if n <= 0:
        return "Podaj liczbe wieksza od zera"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_rek(n-1) + fib_rek(n-2)


wynik = fib_rek(6)
print(wynik)
