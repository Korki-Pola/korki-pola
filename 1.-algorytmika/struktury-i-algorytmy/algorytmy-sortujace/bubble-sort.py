from utils import test


def bubble_sort(array: list[int]) -> list[int]:
    # global counter nie jest czescia algorytmu - sluzy tylko jako benchmark
    global counter

    n = len(array)
    continue_sorting = True
    while continue_sorting:
        count = 0
        for left_index in range(n - 1):
            counter += 1
            right_index = left_index + 1

            left = array[left_index]
            right = array[right_index]

            if left > right:
                array[right_index] = left
                array[left_index] = right
                count += 1
        continue_sorting = count != 0

    return array


if __name__ == "__main__":
    counter = 0
    array = [8, 7, 5, 3, 2, 1]
    sorted_array = bubble_sort([x for x in array])
    print(f'counter: {counter}')
    print(f'array: {array}')
    print(f'sorted_array: {sorted_array}')

    test(bubble_sort)
    test(bubble_sort)
    test(bubble_sort)
