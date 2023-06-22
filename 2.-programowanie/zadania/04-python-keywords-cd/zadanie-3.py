val_1 = float(input('Wpisz pierwszą wartosc calkowita: '))
val_2 = float(input('Wpisz drugą wartosc całkowitą: '))

suma = val_1 + val_2
roznica = val_1 - val_2
iloraz = val_1 // val_2
iloczyn = val_1 * val_2


print(f'Suma to: {suma}.')
print(f'Różnica to: {roznica}.')

print(f'Iloraz to: {iloraz}.')

warunek1 = iloraz == 0
warunek2 = ValueError

if warunek1:

try:
    val_1 = 0
    val_2 = 0
    z = val_1/val_2

except ZeroDivisionError as ZeroDivisionErrorMessage:
    print(f'Nie mozesz dzielic przez zero!')

elif warunek2:

except ValueError as ValueErrorMessage:
    print('ValueErrorMessage')
#try:
 #   val_1 = 1
  #  val_2 = 0
    # wyrzuca (throws) ZeroDivisionError
   # print(val_1 / val_2)

#try:

#except ZeroDivisionError as zeroDivisionErrorMessage:
 #   print(zeroDivisionErrorMessage)


#try:
 #   val_1 = int(input("Podaj wartosc calkowita: "))
#except ValueError as valueErrorMessage:
 #   num_3 = 0
  #  print("Nie umiesz czytać? Podaj wartość calkowita!")

print(f'Iloczyn to: {iloczyn}.')
#elif warunek2:
 #   print(f'Wprowadz liczbę!')


#WIP