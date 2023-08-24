# 11. **Suma Cyfr**: Przeanalizuj program i zmien go tak aby dzialal przy uzyciu petli `while`.
# liczba = 12345
liczba = 12345
suma = 0

while liczba > 0:
    # liczba xyz % 10 = z
    # liczba xyz // 10 = xy

    cyferka =liczba % 10
    liczba = liczba // 10
    suma = suma + cyferka
    
print(suma)


