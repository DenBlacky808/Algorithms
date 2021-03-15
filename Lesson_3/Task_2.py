import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

second_array = [i for i in range(len(array)) if array[i] % 2 == 0]
print(second_array)
