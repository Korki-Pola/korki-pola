#13. **Sekwencja Collatza**: Zacznij od liczby `n`. Jeśli `n` jest parzysta, podziel ją przez 2.
# Jeśli `n` jest nieparzysta, pomnóż ją przez 3 i dodaj 1. Powtarzaj proces z nową wartością `n`, aż `n` stanie się 1.

liczba = int(input("Podaj liczbe: "))

while liczba != 1:
    print(liczba)
    if liczba % 2 == 0:
        liczba = liczba // 2
    else:
        liczba = liczba * 3 + 1
print(liczba)
