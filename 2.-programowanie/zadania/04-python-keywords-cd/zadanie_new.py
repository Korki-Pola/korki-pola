print('Calculator')
#def calculate():
 #   operation =input('''suma = float(val_1) + float(val_2)
#roznica = float(val_1) - float(val_2)
#iloraz = float(val_1) / float(val_2)
#iloczyn = float(val_1) * float(val_2)''')

val_1 = float(input('Wprowadz pierwszą dowolną liczbę: '))
val_2 = float(input('Wprowadz drugą dowolną liczbę: '))

result = float(input('Podaj operator jaki chcesz użyć: '))

suma = float(val_1) + float(val_2)
roznica = float(val_1) - float(val_2)
iloraz = float(val_1) / float(val_2)
iloczyn = float(val_1) * float(val_2)

try:
    if result == '+':
        print(f'Suma to: {suma}.')

    elif result == '-':
        print(f'Różnica to: {roznica}.')

    elif result == '*':
        print(f'Iloraz to: {iloraz}.')

    else:
        print(f'Iloczyn to: {iloczyn}.')

except:
        val_1 = 0.0
        val_2 = 0.0
    dane_niepoprawne = True
while dane_niepoprawne:
    try:
        val_1 = float(input('Wpisz pierwszą dowolną liczbę: '))
        val_2 = float(input('Wpisz drugą dowolną liczbę: '))
        dane_niepoprawne = False
    except ValueError:
        print("Podales bledna wartosc - nalezy podac liczbe!")

suma = val_1 + val_2
roznica = val_1 - val_2
iloczyn = val_1 * val_2

iloraz = 0.0
try:
    iloraz = val_1 / val_2
except ZeroDivisionError:
    iloraz = 'Proba dzielenia przez zero'

again()
def again():
    calc_again = input('''
Chcesz jeszcze raz coś obliczyć?
Napisz T dla TAK albo N dla NIE.
''')

    if calc_again.upper() == 'T':
        calculate()
    elif calc_again.upper() == 'N':
        print('Do zobaczenia później.')
    else:
        again()

calculate()
