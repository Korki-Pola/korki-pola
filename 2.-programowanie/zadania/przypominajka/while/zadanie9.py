# 9. **Tabliczka Mnożenia**: Wydrukuj tabliczkę
# mnożenia dla liczby podanej przez użytkownika
# przy użyciu pętli `while`.

# liczba_podstawowa_tabliczki_mnozenia
liczba = 0
while True:
    try:
        liczba = int(input("Podaj swoja liczbe: "))
        break
    except ValueError:
        continue

for x in range(1, 11):
    print(f'{x} * {liczba} = {x * liczba}')
