val_1 = float(input('Wpisz pierwszą wartosc calkowita: '))
val_2 = float(input('Wpisz drugą wartosc całkowitą: '))

suma = val_1 + val_2
roznica = val_1 - val_2
iloraz = val_1 // val_2
iloczyn = val_1 * val_2


warunek1 = iloraz == 0

except ZeroDivisionError as ZeroDivisionErrorMessage:
    print(f'Nie mozesz dzielic przez zero!')


try:
    val_1 = 1
    val_2 = 0
    # wyrzuca (throws) ZeroDivisionError
    print(val_1 / val_2)

try:
except ZeroDivisionError as zeroDivisionErrorMessage:
    print(zeroDivisionErrorMessage)
except IndexError as indexErrorMessage:
    print(indexErrorMessage)

try:
    val_1 = int(input("Podaj wartosc calkowita: "))
except ValueError as valueErrorMessage:
    num_3 = 0
    print("Nie umiesz czytać? Podaj wartość calkowita!")

print(f'Suma to: {suma}.')
print(f'Różnica to: {roznica}.')
print(f'Iloraz to: {iloraz}.')
print(f'Iloczyn to: {iloczyn}.')
#elif warunek2:
 #   print(f'Wprowadz liczbę!')
