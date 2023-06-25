class MyError(Exception):
    pass

imie = input('Podaj imie: ')
nazwisko = input('Podaj nazwisko: ')

wiek = 0
wiek_incorrect = True
while wiek_incorrect:
    try:
        # int() podniesie ValueError jezeli input zwroci cokolwiek co nie jest liczba calkowita czyli "4.32432", "", "sdf"
        wiek = int(input('Podaj swoj wiek: '))

        # sprawdzanie wieku PIERWSZY SPOSOB
        if wiek < 0:
            raise MyError

        wiek_incorrect = False
    except ValueError:
        print('Podaj liczbe!')
    # sprawdzanie wieku PIERWSZY SPOSOB ciag dalszy
    except MyError:
        print('Wiek nie moze byc mniejszy od 0!')

    # sprawdzanie wieku DRUGI SPOSOB
    # if wiek < 0:
    #     wiek_incorrect = True
    #     print('Wiek nie moze byc mniejszy od 0!')



print(f'Czesc, {imie} {nazwisko}. Masz {wiek} lat')
