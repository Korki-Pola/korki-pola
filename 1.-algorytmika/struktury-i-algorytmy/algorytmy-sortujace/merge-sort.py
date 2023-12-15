from utils import test


def merge_sort(array: list[int]) -> list[int]:
    global counter

    if len(array) <= 1:
        return array

    mid_index = len(array) // 2
    left = array[:mid_index]
    right = array[mid_index:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    i = 0
    j = 0
    k = 0
    while i < len(left_sorted) and j < len(right_sorted):
        counter += 1
        if left_sorted[i] < right_sorted[j]:
            array[k] = left_sorted[i]
            i += 1
        else:
            array[k] = right_sorted[j]
            j += 1
        k += 1

    while i < len(left_sorted):
        counter += 1
        array[k] = left_sorted[i]
        i += 1
        k += 1

    while j < len(right_sorted):
        counter += 1
        array[k] = right_sorted[j]
        j += 1
        k += 1

    return array


if __name__ == "__main__":
    counter = 0
    array = [0, 9, 8, 3, 4, 2, 7, 5, 2, 3, 4, 2, 3, 8, 9, 6, 7]
    sorted_array = merge_sort([x for x in array])
    print(f'counter: {counter}')
    print(f'array: {array}')
    print(f'sorted_array: {sorted_array}')

    test(merge_sort)
    test(merge_sort)
    test(merge_sort)
