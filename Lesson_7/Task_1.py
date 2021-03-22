import random


def pzr_sort(array):
    n = 1
    while n < len(array):
        is_sorted = True
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        if is_sorted:
            break
        n += 1


data = [random.randrange(-100, 100) for _ in range(10)]
print(data)
pzr_sort(data)
print(data)
