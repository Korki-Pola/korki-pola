def binarna_do_dziesietna():
    binarna = '010111001'

    suma = 0
    lista_bin = list(binarna)
    lista_bin.reverse()
    for (indeks, znak) in enumerate(lista_bin):
        znak_int = int(znak)
        wartosc = znak_int * 2 ** indeks
        suma += wartosc

    print('Pierwszy sposob:')
    print(f'binarna: {binarna} => dziesietna: {suma}', end='\n\n')

    suma = 0
    lista_bin = list(binarna)
    len_lista_bin = len(lista_bin)
    for indeks in range(len_lista_bin):
        potega = len_lista_bin - indeks - 1
        znak = lista_bin[indeks]
        znak_int = int(znak)
        wartosc = znak_int * 2 ** potega
        suma += wartosc

    print('Drugi dposob:')
    print(f'binarna: {binarna} => dziesietna: {suma}', end='\n\n')


def dziesietna_do_binarna():
    dziesietna = '35'
    dziesietna_int = int(dziesietna)

    lista_bin = []
    while dziesietna_int != 0:
        (dziesietna_int, cyfra_bin) = divmod(dziesietna_int, 2)
        lista_bin.append(str(cyfra_bin))
    lista_bin.reverse()

    binarna = ''.join(lista_bin)
    print(f'dziesietna: {dziesietna} => binarna: {binarna}', end='\n\n')

def szestnastkowa_do_dziesietna():
    slownik_16_do_10: dict[str, int] = {}

    for x in range(10):
        slownik_16_do_10[str(x)] = x

    for (i, x) in enumerate(list('abcdef')):
        slownik_16_do_10[x] = i + 10

    pprint(slownik_16_do_10)

    szesnastkowa = 'ff'
    lista_szesnastkowa = list(szesnastkowa)
    lista_szesnastkowa.reverse()
    suma = 0
    for (indeks, znak) in enumerate(lista_szesnastkowa):
        znak_int = slownik_16_do_10[znak]
        wartosc = znak_int * 16 ** indeks
        suma += wartosc

        print(f'szesnastkowa: {szesnastkowa} => dziesietna: {suma}', end='\n\n')

def dziesietna_do_szesnastkowa():
    slownik_10_do_16: dict[int,str] = {}

    for x in range(10):
        slownik_10_do_16[x] = str(x)

    for (i, x) in enumerate(list('abcdef')):
        slownik_10_do_16[i + 10] = x

    pprint(slownik_10_do_16)

    dziesietna = '255'
    dziesirtna_l = int(dziesietna)
    cyfry_16 = []
    while dziesirtna_l  != 0:
        (dziesirtna_l, mod) = divmod(dziesirtna_l, 16)
        wartosc = slownik_10_do_16[mod]
        cyfry_16.append(wartosc)
    cyfry_16.reverse()
    szesnastkowa = "".join(cyfry_16)
    print(f'dziesietna: {dziesietna} => szesnastkowa: {szesnastkowa}', end='\n\n')
