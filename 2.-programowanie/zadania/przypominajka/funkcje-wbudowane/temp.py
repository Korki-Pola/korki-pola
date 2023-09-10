from random import randint, random

with open('./zadanie13_input.txt', 'w') as file:
    for _ in range(10):
        end = randint(10, 20)
        m = 1 if round(random()) == 0 else -1
        lista = [x for x in range(0, end * m, m)]
        print(lista, file=file)
