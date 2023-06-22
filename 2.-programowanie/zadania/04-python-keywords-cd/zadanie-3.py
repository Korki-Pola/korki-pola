val_1 = 0.0
val_2 = 0.0
dane_niepoprawne = True
while dane_niepoprawne:
    try:
        # Moze wyrzucic ValueError jezeli uzytkownik poda np.: 'a'
        val_1 = float(input('Wpisz pierwszą dowolną liczbę: '))
        # Moze wyrzucic ValueError jezeli uzytkownik poda np.: 'a'
        val_2 = float(input('Wpisz drugą dowolną liczbę: '))
        dane_niepoprawne = False
    except ValueError:
        print("Podales bledna wartosc - nalezy podac liczbe!")

suma = val_1 + val_2
roznica = val_1 - val_2
iloczyn = val_1 * val_2

# moze wyrzucic ZeroDivisionError
iloraz = 0.0
try:
    iloraz = val_1 / val_2
except ZeroDivisionError:
    iloraz = 'Proba dzielenia przez zero'

print(f'Suma to: {suma}.')
print(f'Różnica to: {roznica}.')
print(f'Iloczyn to: {iloczyn}.')
print(f'Iloraz to: {iloraz}.')