import random
import timeit
import cProfile


SIZE_1 = 15
SIZE_2 = 30
SIZE_3 = 60
SIZE_4 = 120
SIZE_5 = 240
SIZE_6 = 480
SIZE_7 = 960

MIN_ITEM = 0
MAX_ITEM = 10
array_15 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_1)]
array_30 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_2)]
array_60 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_3)]
array_120 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_4)]
array_240 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_5)]
array_480 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_6)]
array_960 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_7)]


def max_cnt(array_in):
    cnt_dict = {}
    frq = 1
    repeat_number = None
    for item in array_in:
        if item in cnt_dict:
            cnt_dict[item] += 1
        else:
            cnt_dict[item] = 1
        if cnt_dict[item] > frq:
            frq = cnt_dict[item]
            repeat_number = item
    return repeat_number


# lst = [2, 2, 5, 5, 7, 8, 9, 10, 10, 10]
# print(max_cnt(lst))

print(timeit.timeit('max_cnt(array_15)', number=1000, globals=globals()))   # 0.003181919999999998
print(timeit.timeit('max_cnt(array_30)', number=1000, globals=globals()))   # 0.004829841999999994
print(timeit.timeit('max_cnt(array_60)', number=1000, globals=globals()))   # 0.009556648000000001
print(timeit.timeit('max_cnt(array_120)', number=1000, globals=globals()))   # 0.040001782
print(timeit.timeit('max_cnt(array_240)', number=1000, globals=globals()))   # 0.066344887
print(timeit.timeit('max_cnt(array_480)', number=1000, globals=globals()))   # 0.11694072
print(timeit.timeit('max_cnt(array_960)', number=1000, globals=globals()))   # 0.268649696

cProfile.run('max_cnt(array_240)')

# 4 function calls in 0.000 seconds
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Task_4_3.py:20(max_cnt)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
