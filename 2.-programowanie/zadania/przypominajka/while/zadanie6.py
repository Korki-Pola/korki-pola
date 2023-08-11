# 6. **Suma Liczb**: Używając pętli `while`, poproś użytkownika
# o wprowadzenie liczb i sumuj je, aż użytkownik wpisze 'stop'.
suma = 0
wprowadzona_liczba = input("Wprowadz liczbe lub wpisz 'stop', aby zakonczyc program: ")

while wprowadzona_liczba != 'stop':
    liczba = int(wprowadzona_liczba)
    suma += liczba
    wprowadzona_liczba = input("Wprowadz liczbe lub wpisz 'stop', aby zakonczyc program: ")

print("Suma wprowadzonych liczb to:" f' {suma}')

