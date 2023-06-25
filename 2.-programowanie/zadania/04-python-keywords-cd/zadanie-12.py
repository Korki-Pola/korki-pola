lista = []

wants_to_quit = False
while not wants_to_quit:
    # Pytanie o element
    element = None
    element_correct = False
    while not element_correct:
        try:
            mozliwy_element = input(
                'Podaj element albo napisz "stop" aby zatrzymac pobieranie: ')

            if mozliwy_element == 'stop':
                wants_to_quit = True
                break

            element = int(mozliwy_element)
            element_correct = True
        except ValueError:
            print('Element musi byc liczba!')

    # Dodanie pobranego elementu do listy
    if (wants_to_quit == False):
        lista.append(element)
        print(f'Aktualny stan listy: {lista}')

print(f'Najwiekszy element listy to: {max(lista)}')
