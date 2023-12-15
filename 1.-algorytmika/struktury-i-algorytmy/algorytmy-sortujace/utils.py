from copy import deepcopy
from functools import reduce
from random import randint
from typing import Callable, TypedDict, List


class Options(TypedDict):
    range_start: int
    range_stop: int
    length: int


def test(sorting_func: Callable[[List[int]], List[int]], array: list[int] = None):
    correct_array: list[int] = []
    if array is None:
        (array, correct_array) = get_arrays()
    else:
        correct_array = sorted(array)

    sorted_array = sorting_func(deepcopy(array))

    passed = reduce(
        lambda acc, x: acc and x[0] == x[1],
        zip(correct_array, sorted_array),
        True
    )

    success = "\033[92m\u2713 Success\033[0m"
    failure = "\033[91m\u2717 Failure\033[0m"

    print()
    print(f'array: {array}')
    print(f'correct_array: {correct_array}')
    print(f'sorted_array: {sorted_array}')
    print(success if passed else failure)
    print()


def get_arrays(options: Options = None) -> tuple[list[int], list[int]]:
    default_options: Options = Options(
        reverse=False,
        range_start=-500,
        range_stop=500,
        length=10
    )

    if options is None:
        options = default_options

    for (key, value) in default_options.items():
        try:
            m = options[key]
        except KeyError:
            options[key] = value

    array = [randint(options['range_start'], options['range_stop'])
             for _ in range(options['length'])]

    return (array, sorted(array))
