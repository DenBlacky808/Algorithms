number = input('введите натуральное число ')
odd = 0
even = 0
for i in number:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'четных - {even} нечетных - {odd}')
