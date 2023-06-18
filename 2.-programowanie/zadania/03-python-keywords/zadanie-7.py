fibonacci = [0, 1]
for i in range(2, 10):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    print(fibonacci)
