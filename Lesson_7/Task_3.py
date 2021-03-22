import random


def mdn_square(array):
    for i in range(len(array)):
        small = 0
        equal = 0
        big = 0
        for j in range(len(array)):
            if array[i] < array[j]:
                small += 1
            elif array[i] > array[j]:
                big += 1
            else:
                equal += 1
        equal -= 1

        if small == big or small == equal + big \
                or big == equal + small or (equal > 1 and abs(big - small) < equal):
            return array[i]


SIZE = 2
LIMIT = 50
data = [random.randrange(0, LIMIT) for _ in range(2 * SIZE + 1)]
print(data)
print(mdn_square(data))
