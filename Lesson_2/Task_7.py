def recurs_sum(n):
    if n == 1:
        return 1
    else:
        return n + recurs_sum(n - 1)


num = int(input("Для какого натурального числа будем делать проверку? "))
result_1 = recurs_sum(num)
result_2 = num * (num + 1) / 2

if result_1 == result_2:
    print(f'Для {num} равенство верно!')
else:
    print(f'Что-то пошло не так {result_1}, {result_2}')
