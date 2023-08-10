# 7. **Zgadnij Liczbę**: Pomyśl o liczbie między 1 a 100 i 
# pozwól użytkownikowi ją odgadnąć. Poinformuj użytkownika, 
# czy jego odpowiedź jest za wysoka, za niska lub poprawna.
print("zgadnij o jakiej liczbie mysle!")
liczba = 2
proba = 0

while liczba != proba:
    try:
        proba = int(input("Wprowadz liczbe o ktorej mysle (miedzy 1 a 100): "))
    except ValueError:
        continue

    if proba < liczba:
        print("Liczba ktora wprowadziles jest za niska")
    elif proba > liczba:
        print("Liczba ktora wprowadziles jest za wysoka")
print("Wygrales")