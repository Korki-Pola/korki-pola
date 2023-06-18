ile = int(input('Podaj ile elementów ciągu Fibonacciego chcesz: '))

fibonacci = [1, 1]
if ile < 0:
    print("bledna wartosc")
elif ile < 2:
    print(fibonacci[0:ile])
else:
    for i in range(2, ile):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    print(fibonacci)
