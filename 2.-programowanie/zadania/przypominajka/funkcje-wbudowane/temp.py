from random import randint, random, choice
from string import ascii_letters, digits

with open('./zadanie17_input.txt', 'w') as file:
    for _ in range(10):
        length = randint(3, 5)
        m = choice([1, -1])
        print([x for x in range(0, length * m, m)], file=file)
