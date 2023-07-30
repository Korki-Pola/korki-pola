print('Calculator')

val_1 = 0.0
val_2 = 0.0
dane_niepoprawne = True
while dane_niepoprawne:
    try:
        val_1 = float(input('Wpisz pierwszą dowolną liczbę: '))
        val_2 = float(input('Wpisz drugą dowolną liczbę: '))
        operator = input('Podaj operator jakiego chcesz użyć, do wyboru masz - suma, roznica, iloraz, iloczyn: ')

        if operator not in ['suma', 'roznica', 'iloraz', 'iloczyn']:
            raise KeyError

        dane_niepoprawne = False
    except ValueError:
        print("Podales bledna wartosc - nalezy podac liczbe!")
    except KeyError:
        print("Podales bledny operator")

suma = val_1 + val_2
roznica = val_1 - val_2
iloczyn = val_1 * val_2

iloraz = 0.0
try:
    iloraz = val_1 / val_2
except ZeroDivisionError:
    iloraz = 'Proba dzielenia przez zero. Nie mozna dzielic przez zero!'

if operator == 'suma':
    print(f'Suma to: {suma}.')

elif operator == 'roznica':
    print(f'Różnica to: {roznica}.')

elif operator == 'iloraz':
    print(f'Iloraz to: {iloraz}.')

else:
    print(f'Iloczyn to: {iloczyn}.')

print('Do zobaczenia później :)')

