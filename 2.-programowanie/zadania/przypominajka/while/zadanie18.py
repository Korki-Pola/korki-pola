#18. **Sekwencja Fibonacciego**: Wydrukuj pierwsze `n` liczb w sekwencji Fibonacciego,
# gdzie `n` jest podane przez użytkownika.

n = int(input("Podaj liczbe n: "))

a,b = 0, 1

for i in range(n):
    print(a)
    a,b = b, a + b
