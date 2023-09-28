## Zadanie 25: Funkcje `map`, `filter`, i `reduce`

#**Cel:** Z listy liczb, podnieś liczby parzyste do kwadratu i oblicz ich sumę.

with opoen("./zadanie25_input.txt", "r") as input_file:
    with open("./zadanie25_output.txt", "w") as output_file:
        linijki = input_file.readlines()
        for linijka in linijki:
            def square_num_parzyste(num)
                if num % 2 == 0:
                    return num ** 2
                else:
                    return num

            numbers = list(range(1, 11))
            squared_num = list(map(square_num_parzyste, numbers))
            nieparzyste_num = list(filter(lambda x: x % 2 == 0, squared_num))
            sum_num = reduce(lambda x, y: x+y, nieparzyste_num)
            print(sum_num, file=output_file)