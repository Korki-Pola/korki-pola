def get_ranges(lines: list[str]) -> list[tuple[int, int, bool, bool]]:
    ranges: list[tuple[int, int, bool, bool]] = []
    for line in lines:
        # "(-3,3>\n"
        line = line.strip()
        # "(-3,3>"

        left_open = line[0] == '('
        right_open = line[len(line) - 1] == ')'

        # "(-3,3>"
        line = line[1:len(line) - 1]
        # "-3,3"
        line_nums = line.split(',')
        # ["-3", "3"]

        a = int(line_nums[0])
        b = int(line_nums[1])

        ranges.append((a, b, left_open, right_open))
    return ranges


def check_how_many_odd_numbers(a: int, b: int, left_open: bool, right_open: bool) -> int:
    if left_open:
        a = a + 1

    if right_open:
        b = b - 1

    # dodatkowe wypisywanie do rozjasnienia dzialania algorytmu
    # l = '(' if left_open else '<'
    # r = ')' if right_open else '>'
    # print(f'przedzial: {l}{a},{b + 1}{r}')

    count = 0
    for num in range(a, b + 1):
        if num % 2 == 1:
            count += 1

    # dodatkowe wypisywanie do rozjasnienia dzialania algorytmu
    # print(f'ilosc nparz: {count}')

    return count


def zadanie_1_1(ranges: list[tuple[int, int, bool, bool]], output_file):
    # trzyma numery linii w ktorych stoja przedzialy o najwiekszej ilosc liczb nieparzystych
    range_line_numbers = []
    # trzyma najwieksza ilosc liczb nieparzystych
    biggest_odd_num_count = 0
    for (index, (a, b, left_open, right_open)) in enumerate(ranges):
        # dodatkowe wypisywanie do rozjasnienia dzialania algorytmu
        # print(f'linijka: {index + 1}')

        odd_nums_count = check_how_many_odd_numbers(
            a, b, left_open, right_open)

        if biggest_odd_num_count < odd_nums_count:
            biggest_odd_num_count = odd_nums_count
            range_line_numbers = []

        if odd_nums_count == biggest_odd_num_count:
            range_line_numbers.append(index + 1)

    # Zapisywanie wyniku do 'wyniki1.txt'
    print(biggest_odd_num_count, end=' ', file=output_file)
    for num in range_line_numbers:
        print(num, end=' ', file=output_file)
    print(file=output_file)


def zadanie_1_2(ranges: list[tuple[int, int, bool, bool]], output_file):
    pass


with open("./przedzialy.txt", "r") as input_file:
    with open("./wyniki1.txt", 'w') as output_file:
        lines = input_file.readlines()
        ranges: list[tuple[int, int, bool, bool]] = get_ranges(lines)

        zadanie_1_1(ranges, output_file)

