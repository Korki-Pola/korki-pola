# 19. **Kalkulator Prostego Oprocentowania**: Nieustannie pytaj użytkownika o kwotę główną, 
# stopę oprocentowania i czas (w latach). Oblicz i wyświetl proste oprocentowanie przy 
# użyciu formuły: `Proste Oprocentowanie = (Kwota główna x Stopa x Czas) / 100`.
# Zakończ, gdy użytkownik powie 'nie'.

while True:
    str_od_uzytkownika = input("Podaj kwote, stope i czas (w formacie: <kwota>, <stopa>, <czas>). Wprowadz 'nie' aby zakonczyc dzialanie programu:\n")

    if str_od_uzytkownika == 'nie':
        break

    lista_wartosci = str_od_uzytkownika.split(', ')

    for index in range(len(lista_wartosci)):
        element = lista_wartosci[index]
        lista_wartosci[index] = float(element)

    [kwota, stopa ,czas] = lista_wartosci

    proste_oprocentowanie = (kwota * stopa * czas) / 100

    print(f'Proste oprocentowanie: {proste_oprocentowanie}')


# user_input = '10000, 0.20, 1.5'.split(', ')
# print(user_input)
# [kwota, stopa, czas] = user_input
# print(kwota, stopa, czas)
