# 10. **Silnia**: Oblicz silnię liczby przy użyciu pętli `while`.
golomp = 0
while True:
    try:
        golomp = int(input("Podaj liczbe: "))
        break
    except ValueError:
        continue

if golomp < 0:
    print("Wartosc silni nie istneje")
elif golomp > 0:
    iloczyn = 1
    for i in range(1, golomp + 1):
        iloczyn = iloczyn * i

    print(iloczyn)
else:
    print(1)
