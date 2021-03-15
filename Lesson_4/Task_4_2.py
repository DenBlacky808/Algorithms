import random
import timeit
import cProfile


SIZE_1 = 15
SIZE_2 = 30
SIZE_3 = 60
SIZE_4 = 120
SIZE_5 = 240
MIN_ITEM = 0
MAX_ITEM = 10
array_15 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_1)]
array_30 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_2)]
array_60 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_3)]
array_120 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_4)]
array_240 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_5)]


def max_cnt(array_in):
    repeat_number = None
    frq = 1
    for i in range(len(array_in)):
        temp_var = 1
        for j in range(i + 1, len(array_in)):
            if array_in[i] == array_in[j]:
                temp_var += 1
        if temp_var > frq:
            frq = temp_var
            repeat_number = array_in[i]

    return repeat_number


# lst = [2, 2, 5, 5, 7, 8, 9, 10, 10, 10]
# print(max_cnt(lst))

print(timeit.timeit('max_cnt(array_15)', number=1000, globals=globals()))   # 0.038777797
print(timeit.timeit('max_cnt(array_30)', number=1000, globals=globals()))   # 0.085467363
print(timeit.timeit('max_cnt(array_60)', number=1000, globals=globals()))   # 0.294511312
print(timeit.timeit('max_cnt(array_120)', number=1000, globals=globals()))   # 1.246790759
print(timeit.timeit('max_cnt(array_240)', number=1000, globals=globals()))   # 4.841161119000001

cProfile.run('max_cnt(array_240)')

# 245 function calls in 0.002 seconds
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#      1    0.006    0.006    0.006    0.006 Task_4_2.py:20(max_cnt)
#      1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#    241    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
