#17. **Znajdź Liczby Pierwsze**: Wydrukuj wszystkie liczby pierwsze między 2 a liczbą `n`
# podaną przez użytkownika. (Ladniejsze rozwiazanie korzysta z listy w ktorej
# sa przechowywywane wszystkie dotad odkryte liczby pierwsze)

n = int(input("Podaj liczbe n: "))
liczby_pierwsze = [2]

for liczba in range(3, n + 1):
    czy_pierwsza = True

    for dzielnik in liczby_pierwsze:
        if liczba % dzielnik == 0:
            czy_pierwsza = False
            break

        if czy_pierwsza:
            liczby_pierwsze.append(liczba)
            break

print(liczby_pierwsze)
