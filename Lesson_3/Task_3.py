"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_pos = 0
max_pos = 0
min_num = array[len(array) - 1]
max_num = array[0]

for i in range(len(array)):
    if array[i] < min_num:
        min_num = array[i]
        min_pos = i
    elif array[i] > max_num:
        max_num = array[i]
        max_pos = i
array[min_pos] = max_num
array[max_pos] = min_num
print(array)
