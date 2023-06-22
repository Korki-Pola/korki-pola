# 1. n jest rowne 0 lub jest mniejsze od zera
# 2. n jest wieksze od zera
n = int(input('Podaj liczbe n: '))

# 1. - 2. inicjalizacja sumy
suma = 0
# 1. brak wejscia w petle bo warunek
# i <= n nigdy nie bedzie True
# 2. realizacja petli od 1 .. n
i = 1
while i <= n:
    suma += i
    i += 1

print(f'Suma to: {suma}')