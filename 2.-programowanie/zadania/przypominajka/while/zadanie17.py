#17. **Znajdź Liczby Pierwsze**: Wydrukuj wszystkie liczby pierwsze między 2 a liczbą `n`
# podaną przez użytkownika. (Ladniejsze rozwiazanie korzysta z listy w ktorej
# sa przechowywywane wszystkie dotad odkryte liczby pierwsze)

#n = int(input("Podaj liczbe n: "))

#liczba = 2
#while liczba <= n:
#    jest_pierwsza = True

 #   for i in range(2, liczba):
  #      if liczba % i == 0:
   #         jest_pierwsza = False
    #        break

     #   if jest_pierwsza:
      #      print(liczba)

    #liczba += 1

    #2 wip

#n = int(input('Podaj liczbe n: '))
#liczby_pierwsze = []

#for liczba in range(2, n + 1):
 #   czy_pierwsza = True
  #  dzielnik = 2

#while liczba <= n:
 #   if liczba % dzielnik == 0:
 #       czy_pierwsza = False
  #      break
   # dzielnik += 1

#if czy_pierwsza:
 #   liczby_pierwsze.appened(liczba)

#print(liczby_pierwsze)

#3 wip z lista

n = int(input("Podaj liczbe n: "))
liczby_pierwsze = [2]

for liczba in range(3, n + 1):
    czy_pierwsza = True

    for dzielnik in liczby_pierwsze:
        if liczba % dzielnik == 0:
            czy_pierwsza = False
            break

        if czy_pierwsza:
            liczby_pierwsze.append(liczba)
print(liczby_pierwsze)
