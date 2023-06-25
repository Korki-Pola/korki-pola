
liczba = 0.0
input_incorrect = True
while input_incorrect:
    try:
        liczba = int(input('Wprowadz liczbę: '))
        input_incorrect = False
    except ValueError:
        print(f'Podaj liczbe!')

if liczba % 2 == 0:
    print('Liczba jest parzysta.')
else:
    print('Liczba jest nieparzysta.')
