def iteracja_1(n: int) -> None:
    print('ITERACJA - START')

    for i in range(n):
        print(f'Hello world {i}')

    print('ITERACJA - KONIEC')


def rekurencja_1(n: int, i=0) -> None:
    print('REKURANCJA - START')
    if i < n:
        print(f'Hello world {i}')

        rekurencja_1(n, i + 1)
        print('REKURANCJA - KONIEC')
    else:
        print('REKURANCJA - KONIEC')
        return


def iteracja_2(ciag: str, n: int) -> str:
    nowy_ciag = ''

    for _ in range(n):
        nowy_ciag += ciag

    return nowy_ciag


def rekurencja_2(ciag: str, n: int, orginalny_ciag='') -> str:
    if orginalny_ciag == '':
        orginalny_ciag = ciag

    if n == 1:
        return ciag

    return rekurencja_2(ciag + orginalny_ciag, n - 1, orginalny_ciag)


# stworz funkcje ktora bedzie dodawala dana liczbe a do siebie n razy
def iteracja_3(a: int, n: int) -> int:
    result = 0
    for _ in range(n):
        result += a
    return result


# jezeli potrzebujesz dopisac jakies wartosci pomocnicze to je dopisz
def rekurencja_3(a: int, n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return a
    else:
        return a + rekurencja_3(a, n - 1)

# ITERACJA - to wykonywanie czegos w petli
# REKURENCJA - to wywolywanie funkcji przez sama siebie

print(iteracja_3(3, 10))    # wypisuje 30
print(rekurencja_3(3, 10))  # wypisuje 30
print(iteracja_3(0, 10))    # wypisuje 0
print(rekurencja_3(0, 10))  # wypisuje 0
print(iteracja_3(-1, 10))   # wypisuje -10
print(rekurencja_3(-1, 10))  # wypisuje -10


# moj_ciag = 'DuPa'
# print(iteracja_2(moj_ciag, 10))
# print(rekurencja_2(moj_ciag, 10))

# iteracja(20)
# rekurencja_1(20)
