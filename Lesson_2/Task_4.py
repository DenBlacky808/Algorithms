def func_row(n):
    sum_1 = 1
    for i in range(0, n + 1):
        sum_1 = sum_1 + sum_1/(-2)
    return sum_1


num = int(input("Введите натуральное число "))
print(func_row(num))
