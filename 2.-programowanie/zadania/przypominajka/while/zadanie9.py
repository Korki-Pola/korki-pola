# 9. **Tabliczka Mnożenia**: Wydrukuj tabliczkę
# mnożenia dla liczby podanej przez użytkownika
# przy użyciu pętli `while`.
guess = int(input("Podaj swoja liczbe: "))
# guess = 0
i = range(1, 11)
wynik = i * guess
# wynik = 0
while guess == 0:
    for i in range(1, 11):
        try:
            print(f'{wynik}')
            guess += 1
        except ValueError:
            print("Podaj liczbe!")
