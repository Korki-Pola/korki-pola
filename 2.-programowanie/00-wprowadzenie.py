# do zmiennej a zostaje przypisana wartosc 4
a = 4

# print to funkcja wypisujaca do wyjscia standardowego
# wypisanie wartosci spod zmiennej a przy uzyciu funkcji print
print(a)

# -------------------------------------- #
# TYPY DANYCH W PYTHONIE I ICH OPERATORY #
# -------------------------------------- #

# WARTOSCI LICZBOWE
# 1. int -> integer (pol. wartosc calkowita)
int_1 = 12
int_2 = 3

# 2. float -> floating point (pol. wartosc zmiennoprzecinkowa)
float_1 = 3.0
float_2 = 0.00000001

# OPERATORY WARTOSCI LICZBOWYCH
# 1. dodawanie
print('dodawanie')
print(int_1 + int_2)
print(int_1 + float_1)

# 2. odejmowanie
print('odejmowanie')
print(int_1 - int_2)
print(int_1 - float_1)

# 3. mnozenie
print('mnozenie')
print(int_1 * int_2)
print(int_1 * float_1)

# 4. potegowanie
print('potegowanie')
print(int_1 ** int_2)
print(int_1 ** float_1)

# 5. zwykle dzielenie
print('zwykle dzielenie')
print(int_1 / int_2)

# 6. dzielenie calkowite (tj. wynik bez ulamka)
print('dzielenie calkowite')
print(int_1 // int_2)

# 7. modullo (reszta z dzielenia)
print('modullo')
print(int_1 % int_2)

# WARTOSCI LOGICZNE
print(True)
print(False)

# OPERATORY LOGICZNE
x = 3
y = 5

# 1. mniejsze, mniejsze-rowne, wieksze, wieksze-rowne
print(x < y)
print(x <= y)
print(x > y)
print(x >= y)

# 2. rowne
print(x == y)
print(x is y)

# 3. nierowne
print(x != y)
print(x is not y)

# 4. koniunkcja i alternatywa (i / lub) (and / or)
print(x and y)
print(x or y)

# WARTOSCI TEKSTOWE
text_1 = 'Hello world!'
text_2 = "Hello world! Give me your name: "
text_3 = ''
text_4 = ""

# Operatory wartosci textowych
# wypisywanie
print(text_1)

# wprowadzanie danych przez uzytkownika
user_input = input(text_2)
print(user_input)

# odczyt wartosci tekstowej od 0 do 3 indeksu (bez wartosci na 3 indeksie)
print(text_1[0:3])

# LISTY
list_1 = [0, 2, -4, 10.0, 12.3 * 6, 'text 123', True]

print(list_1)
print(list_1[0], list_1[-7])

list_1[0] = 1337

print(list_1)

# SLOWNIKI
dict_1 = {'klucz': 10, 'klucz2': {1341242342314: 13}, 0: {'key': [123123, 123124, '234234324']}}

print(dict_1)
