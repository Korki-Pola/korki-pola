#14. **Weryfikacja Wprowadzonych Danych**: Nieustannie pytaj użytkownika o wprowadzenie liczby między 1 a 10.
# Jeśli wpiszą wartość spoza tego zakresu, zapytaj ich ponownie.

liczba = 0
while liczba < 1 or liczba > 10:
    flaga = False
    try:
        liczba = float(input("Wprowadz liczbe miedzy 1 a 10: "))
    except ValueError:
        flaga = True
        print("Wprowadziles niepoprawna liczbe! To co podales to nie jest liczba")

    if not flaga and (liczba < 1 or liczba > 10):
        print("Wprowadziles niepoprawna liczbe! To co podales nie jest w zakresie")

print("Wprowadziles poprawna liczbe!")
