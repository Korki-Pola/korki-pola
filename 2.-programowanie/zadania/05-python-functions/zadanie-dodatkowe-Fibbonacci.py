def fibonacci(start, koniec):

    start = ('Podaj początkowy indeks: ')
    koniec = ('Podaj końcowy indeks: ')

    a, b= 0,1
    for i in range(koniec):
        if i >= start:
            print(a)
        a, b = b, a + b

def fibonacci():
    flag = True
    while flag:
        pass


fibonacci(start, koniec)

def main():
    fibonacci()

if __name__ =="__main__":
    main()