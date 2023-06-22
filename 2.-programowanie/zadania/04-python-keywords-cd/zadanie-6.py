n = int(input("Podaj wartosc: "))

nums_dict = {}
for x in range(1, n + 1):
    nums_dict[x] = x ** 2

print(nums_dict)
