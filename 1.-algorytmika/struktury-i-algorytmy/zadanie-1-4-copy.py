#napisac funkcje liczaca czynnki pierwsze liczby

#def oblicz_czynniki_pierwsze(N: int) -> list:
    #czynniki = []
   # liczby_pierwsze = []

    #for liczba in range(2, int(N ** 0.5) + 1):
        #jest_pierwsza = True
        #for p in liczby_pierwsze:
         #   if liczba % p == 0:
        #        jest_pierwsza = False
       #         break
      #  if jest_pierwsza:
     #       liczby_pierwsze.append(liczba)

    #for p in liczby_pierwsze:
    #    while N % p == 0:
   #         czynniki.append(p)
  #          N = N // p
 #   if N > 1:
#        czynniki.append(N)

#N = int(input("Podaj liczbe N: "))
#czynniki = oblicz_czynniki_pierwsze(N)
#print(f'Czynniki pierwsze liczby {N} to: {czynniki}')

#return czynniki


def oblicz_czynniki_pierwsze(N):
    czynniki = []
    for liczba in range(2, int(N ** 0.5) + 1):
       while N % liczba == 0:
           czynniki.append(liczba)
           N//= liczba
    if N >1:
        czynniki.append(N)
    return czynniki

liczba = int(input("Podaj liczbe: "))
czynniki_pierwsze = oblicz_czynniki_pierwsze(liczba)
print(f'Czynniki pierwsze liczby {liczba} to: {czynniki_pierwsze}')

























