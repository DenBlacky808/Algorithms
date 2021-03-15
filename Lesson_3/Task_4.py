import random

SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

array_set = set(array)
repeat_number = None
qnt_repeat = 0
for item in array_set:
    qnt = array.count(item)
    if qnt > qnt_repeat:
        qnt_repeat = qnt
        repeat_number = item

print(repeat_number)
