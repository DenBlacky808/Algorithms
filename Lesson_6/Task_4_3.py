import random
import sys


SIZE_5 = 240
MIN_ITEM = 0
MAX_ITEM = 10
array_240 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_5)]


cnt_dict = {}
frq = 1
repeat_number = None
for item in array_240:
    if item in cnt_dict:
        cnt_dict[item] += 1
    else:
        cnt_dict[item] = 1
    if cnt_dict[item] > frq:
        frq = cnt_dict[item]
        repeat_number = item
print(repeat_number)

sum_usage = 0
var_list = [cnt_dict, frq, array_240, repeat_number, item]
for variable in var_list:
    sum_usage += sys.getsizeof(variable)

print(sum_usage)
