# 8. **Hasło**: Nieustannie pytaj użytkownika o
# hasło, dopóki nie poda poprawnego.
print("Podaj poprawne hasło :)")
proba = input("Wpisz hasło: ")
haslo = "1234"

while proba != haslo:
    # if haslo != klucz:
    print("Podeles zle haslo")
    proba = input("Podaj hasło: ")

    # if haslo != klucz:

print("Podales prawidlowe haslo!")
