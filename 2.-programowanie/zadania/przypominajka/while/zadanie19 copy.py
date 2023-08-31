# 19. **Kalkulator Prostego Oprocentowania**: Nieustannie pytaj użytkownika o kwotę główną, 
# stopę oprocentowania i czas (w latach). Oblicz i wyświetl proste oprocentowanie przy 
# użyciu formuły: `Proste Oprocentowanie = (Kwota główna x Stopa x Czas) / 100`.
# Zakończ, gdy użytkownik powie 'nie'.

while True:
    str_od_uzytkownika = input("Podaj kwote, stope i czas (uzyj fromatu: <kwota>, <stopa>, <czas>). Aby zakonczyc napisz 'nie': \n")

    if str_od_uzytkownika == 'nie':
        break

    lista_wartosci = str_od_uzytkownika.split(', ')

    for index in range(len(lista_wartosci)):
        element = lista_wartosci[index]
        lista_wartosci[index] = float(element)

    [kwota, stopa, czas] = lista_wartosci

    proste_oprocentowanie = (kwota * stopa * czas) / 100
    
    print(f'Proste oprocentowanie wynosi: {proste_oprocentowanie} ')
