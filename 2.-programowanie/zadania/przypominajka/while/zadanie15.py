#15. **Drukuj Trójkąt**: Poproś użytkownika o podanie liczby, `n`.
# Wydrukuj trójkąt z `*` o `n` wierszach przy użyciu pętli `while`.

n = int(input('Podaj liczbe n: '))

i = 1
while i <= n:
    #print('*' * i)
    print(" " * (n - i) + "*" * (2 * i - 1))
    i += 1
