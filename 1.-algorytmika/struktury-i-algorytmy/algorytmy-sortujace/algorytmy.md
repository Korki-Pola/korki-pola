# 1. Bubble Sort

## Code:

```python
from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

## Details:

- **Best Case**: O(n)
- **Average Case**: O(n^2)
- **Worst Case**: O(n^2)
- **Memory**: O(1)
- **Stable**: Yes
- **Method Used**: Exchanging

# 2. Merge Sort

## Code:

```python
from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
```

## Details:

- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)
- **Memory**: O(n)
- **Stable**: Yes
- **Method Used**: Merging

# 3. Quick Sort

## Code:

```python
from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
```

## Details:

- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n^2)
- **Memory**: O(log n)
- **Stable**: No
- **Method Used**: Partitioning

# 4. Heap Sort

## Code:

```python
from typing import List

def heapify(arr: List[int], n: int, i: int):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
```

## Details:

- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)
- **Memory**: O(1)
- **Stable**: No
- **Method Used**: Selection

# 5. Insertion Sort

## Code:

```python
from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr
```

## Details:

- **Best Case**: O(n)
- **Average Case**:

O(n^2)

- **Worst Case**: O(n^2)
- **Memory**: O(1)
- **Stable**: Yes
- **Method Used**: Insertion
