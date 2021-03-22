import random


def sli_sort(array):
    if len(array) <= 1:
        return array
    left = sli_sort(array[:len(array) // 2])
    right = sli_sort(array[len(array) // 2:])
    i = j = 0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1
    while len(left) > i:
        array[i + j] = left[i]
        i += 1
    while len(right) > j:
        array[i + j] = right[j]
        j += 1
    return array


data = [random.uniform(0, 50) for _ in range(10)]
print(data)
sli_sort(data)
print(data)
