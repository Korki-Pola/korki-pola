mozliwe_minimum = 0
mozliwe_maksimum = 0
while True:
    try:
        mozliwe_minimum = int(input("Podaj minimalna liczbe: "))
        mozliwe_maksimum = int(input("Podaj maksymalna liczbe: "))
        break
    except ValueError:
        continue

maksimum = max(mozliwe_minimum, mozliwe_maksimum)
minimum = min(mozliwe_minimum, mozliwe_maksimum)

dlugosc_przedzialu = maksimum - minimum + 1

while True:
    proba = minimum + dlugosc_przedzialu // 2
    decyzja = input(f"Czy twoja liczba to {proba}? 'za [n]iska/za [w]ysoka/[t]ak to moja liczba': ")

    if decyzja not in ['w', 'n', 't']:
        continue

    if decyzja == 't':
        break

    if decyzja == 'n':
        minimum = proba
    if decyzja == 'w':
        maksimum = proba


    if minimum - maksimum == 0:
        print("Oszukista!!! Foch...")
        break

    dlugosc_przedzialu = maksimum - minimum + 1
    proba = minimum + dlugosc_przedzialu // 2

