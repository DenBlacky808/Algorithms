y = int(input('Введите год '))
if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print('Не високосный')
else:
    print('Високосный')
