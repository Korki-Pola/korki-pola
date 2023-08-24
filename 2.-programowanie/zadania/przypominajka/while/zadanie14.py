#14. **Weryfikacja Wprowadzonych Danych**: Nieustannie pytaj użytkownika o wprowadzenie liczby między 1 a 10.
# Jeśli wpiszą wartość spoza tego zakresu, zapytaj ich ponownie.

liczba = 1
liczba = int(input("Wprowadz liczbe miedzy 1 a 10: "))

while liczba < 1 or liczba > 10:
    try:
        liczba = int(input("Wprowadziles liczbe poza zakresem. Wprowadz liczbe ponownie: "))
    except ValueError:
        print(input("Wprowadz liczbe! : "))

print("Wprowadziles poprawna liczbe!")
