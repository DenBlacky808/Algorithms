import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 1
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

negative_item_pos = 0
negative_item = 0

for item in array:
    if item < negative_item:
        negative_item = item

for i in range(len(array)):
    if array[i] < 0 and abs(array[i]) < abs(negative_item):
        negative_item_pos = i
        negative_item = array[i]
print(negative_item, negative_item_pos)
