import random
import sys


SIZE_5 = 240
MIN_ITEM = 0
MAX_ITEM = 10
array_240 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_5)]


repeat_number = None
frq = 1
for i in range(len(array_240)):
    temp_var = 1
    for j in range(i + 1, len(array_240)):
        if array_240[i] == array_240[j]:
            temp_var += 1
    if temp_var > frq:
        frq = temp_var
        repeat_number = array_240[i]

print(repeat_number)
sum_usage = 0
var_list = [array_240, temp_var, frq, repeat_number, i, j]
for variable in var_list:
    sum_usage += sys.getsizeof(variable)

print(sum_usage)
