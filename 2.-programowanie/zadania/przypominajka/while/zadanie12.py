#12. **Odwróć Liczbę**: Mając daną liczbę, odwróć jej cyfry przy użyciu pętli `while`.

liczba = 12345
odwrocona_liczba = ""

while liczba > 0:
    cyferka = liczba % 10
    liczba = liczba // 10
    odwrocona_liczba += str(cyferka)

odwrocona_liczba = int(odwrocona_liczba)
print(odwrocona_liczba)

# rozwiazanie szymka
# liczba = 12345
# odwrocona_liczba = ''.join(list(reversed(str(liczba))))
# print(odwrocona_liczba)

#2 sposob
#liczba = 12345

#while liczba >0:
   # cyferka = liczba % 10
   # liczba = liczba // 10
  #  print(cyferka, end='')
