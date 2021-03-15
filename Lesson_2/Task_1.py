"""

https://drive.google.com/file/d/1Pyt_wefNM75VjYC7vMThUnjfMt6k1_Lf/view?usp=sharing

"""

operation = 1
while operation != '0':
    print('введите два числа')
    num_1 = int(input('num_1 = '))
    num_2 = int(input('num_2 = '))
    print('введите знак операции')
    operation = input('operation = ')
    if operation == '+':
        result = num_1 + num_2
        print(result)
    elif operation == '-':
        result = num_1 - num_2
        print(result)
    elif operation == '*':
        result = num_1 * num_2
        print(result)
    elif operation == '/':
        if num_2 == 0:
            print('Нельзя делить на ноль!')
        else:
            result = num_1 / num_2
            print(result)
    else:
        print('Ошибка! Введите корректную операцию')
