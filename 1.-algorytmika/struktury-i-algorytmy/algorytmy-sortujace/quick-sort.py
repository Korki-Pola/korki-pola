from utils import test


def swap(array: list[int], i: int, j: int) -> list[int]:
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return array


def choose_pivot_index(array: list[int]) -> int:
    left_index = 0
    left = array[left_index]
    middle_index = len(array) // 2
    middle = array[middle_index]
    right_index = len(array) - 1
    right = array[right_index]

    average = (left + middle + right) / 3
    points = [(left, left_index), (middle, middle_index), (right, right_index)]
    min_distance = float('inf')
    index = 0
    for (point, point_index) in points:
        temp_min_distance = abs(average - point)
        if min_distance > temp_min_distance:
            min_distance = temp_min_distance
            index = point_index

    return index


def quick_sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array

    if len(array) == 2:
        if array[0] > array[1]:
            return swap(array, 0, 1)
        return array

    pivot_index = choose_pivot_index(array)
    last_index = len(array) - 1

    array = swap(array, last_index, pivot_index)
    pivot_index = last_index

    left_index = 0
    right_index = pivot_index - 1
    crossed = False
    while not crossed:
        while array[left_index] < array[pivot_index] and left_index < pivot_index:
            left_index += 1

        while array[right_index] >= array[pivot_index] and right_index >= 0:
            right_index -= 1

        if right_index < left_index:
            crossed = True
        else:
            array = swap(array, left_index, right_index)

    array = swap(array, pivot_index, left_index)
    pivot_index = left_index
    left_partition = quick_sort(array[:pivot_index])
    right_partition = quick_sort(array[pivot_index + 1:])
    return left_partition + [array[pivot_index]] + right_partition


if __name__ == "__main__":
    array = [8, 9, 2, 3, 4, 6, 2, 1, -2]
    print(array)
    print(quick_sort(array))

    test(quick_sort)
    test(quick_sort)
    test(quick_sort)
