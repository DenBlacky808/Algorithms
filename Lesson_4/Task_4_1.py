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
    array_set = set(array_in)
    repeat_number = None
    cnt_repeat = 0
    for item in array_set:
        cnt = array_in.count(item)
        if cnt > cnt_repeat:
            cnt_repeat = cnt
            repeat_number = item

    return repeat_number


# lst = [2, 2, 5, 5, 7, 8, 9, 10, 10, 10]
# print(max_cnt(lst))

print(timeit.timeit('max_cnt(array_15)', number=1000, globals=globals()))   # 0.004254538000000002
print(timeit.timeit('max_cnt(array_30)', number=1000, globals=globals()))   # 0.008713084
print(timeit.timeit('max_cnt(array_60)', number=1000, globals=globals()))   # 0.015396542999999999
print(timeit.timeit('max_cnt(array_120)', number=1000, globals=globals()))   # 0.029859443999999992
print(timeit.timeit('max_cnt(array_240)', number=1000, globals=globals()))   # 0.07157505800000001
print(timeit.timeit('max_cnt(array_480)', number=1000, globals=globals()))   # 0.16183675300000003
print(timeit.timeit('max_cnt(array_960)', number=1000, globals=globals()))   # 0.329998855

cProfile.run('max_cnt(array_960)')

# 15 function calls in 0.000 seconds
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 Task_4_1.py:20(max_cnt)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     11    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#                               результаты

# N	    1 version	            2 version 	        3 version

# 15	0.004254538000000002	0.038777797	        0.003181919999999998
# 30	0.008713084	            0.085467363	        0.004829841999999994
# 60	0.015396542999999999	0.294511312	        0.009556648000000001
# 120	0.029859443999999992	1.246790759     	0.040001782
# 240	0.07157505800000001	    4.841161119000001	0.066344887
# 480   0.16183675300000003                         0.11694072
# 960   0.329998855                                 0.268649696

# По скорости работы можно сделать вывод, что встроенная функция count()
# не так уж плоха и вполне пригодна для решения данной задачи. Сложность решения 1 и 3 линейны.
# Сложность решения 2 квадратична.
# 3 решение показывает небольшой прирост в производительности.
# по отчету cProfile можно сделать вывод, что в первой версии реализации 11 раз обращаемся к функции count.
# Функция count  использует алгоритм Бойера - Мура, что по версии википедии является
# эффективным алгоритмом поиска.
# Однако, 3 решение является своего рода индексацией, поэтому 3-й алгоритм быстрее 1-го и 2-го.
