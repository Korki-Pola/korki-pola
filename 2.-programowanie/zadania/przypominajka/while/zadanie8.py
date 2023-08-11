# 8. **Hasło**: Nieustannie pytaj użytkownika o
# hasło, dopóki nie poda poprawnego.
print("Podaj poprawne hasło :)")
haslo = int(input("Wpisz hasło: "))
klucz = 1234

while haslo != klucz:
    # if haslo != klucz:
    try:
        haslo = int(input("Podaj hasło: "))

    except ValueError:
        # print("Podales prawidlowe haslo!")
        print("Podales bledna wartosc. Sprobuj ponownie")
        continue
    # if haslo != klucz:

print("Podales prawidlowe haslo!")
