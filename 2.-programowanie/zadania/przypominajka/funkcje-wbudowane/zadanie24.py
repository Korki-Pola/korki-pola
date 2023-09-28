## Zadanie 24: Kombinacja funkcji `open`, `read`/`readlines` i `sum`
#
#**Cel:** Odczytaj plik zawierający liczby oddzielone przecinkami i oblicz ich sumę.

with open("./zadanie24_input.txt", "r") as input_file:
    with open("./zadanie24_output.txt", "w") as output_file:
        numbers = file.read().split(",")
        numbers = [int(num)for num in numbers]
        total_sum = sum(numbers)
        print(total_sum, file=output_file)
