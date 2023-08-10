# 6. **Suma Liczb**: Używając pętli `while`, poproś użytkownika o 
# wprowadzenie liczb i sumuj je, aż użytkownik wpisze 'stop'.

suma = 0
wprowadzona_liczba = input("wprowadz liczbe lub wpisz 'stop': ")
while wprowadzona_liczba != 'stop':
    try:
        liczba = float(wprowadzona_liczba)
    except ValueError:
        wprowadzona_liczba = input("zly input! wprowadz liczbe lub wpisz slowo 'stop': ")
        continue

    suma += liczba
    wprowadzona_liczba = input("wprowadz liczbe lub wpisz 'stop': ")

print(f'Suma: {suma}')
