# Algorytm Euklidesa to sposob na uzyskiwanie NWD (najwiekszego wspolnego dzielnika) dwoch liczb. Oto ten algorytm:
# 1.    jeżeli reszta jest równa 0, to NWD(a,b)=b
# 2.    jeżeli reszta jest różna od 0, to przypisujemy liczbie a wartość liczby b,
#       liczbie b wartość otrzymanej reszty, a następnie wykonujemy ponownie punkt 1

def nwd_iter(a: int, b: int) -> int:
    r = a % b

    while r != 0:
        a = b
        b = r
        r = a % b

    return b


def nwd_rek(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return nwd_rek(b, a % b)
