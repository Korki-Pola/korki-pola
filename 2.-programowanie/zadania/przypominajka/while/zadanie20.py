# 20. **Tylko Dodatnie Liczby**: Ciągle akceptuj liczby od użytkownika,
# aż wprowadzi liczbę ujemną. Następnie wydrukuj średnią ze wszystkich wprowadzonych liczb dodatnich.

liczby_dodatnie = []
liczba = int(input("Wprowadz liczbe dodatnia (albo ujemna by zakonczyc): "))

while liczba >= 0:
    liczby_dodatnie.append(liczba)
    liczba = int(input("Wprowadz liczbe dodatnia (albo ujemna by zakonczyc): "))

if len(liczby_dodatnie) > 0:
    srednia = sum(liczby_dodatnie) / len(liczby_dodatnie)
    print("Srednia wszystkich liczb to: ", srednia)
else:
    print("Nie wprowadzono zadnych liczb dodatnich")
