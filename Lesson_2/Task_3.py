number = input("Введите натуральное число ")
number = number.rstrip('0')

number_2 = 0

while int(number) > 0:
    digit = number % 10
    number = number // 10
    number_2 = number_2 * 10
    number_2 = number_2 + digit

print('"Обратное" ему число ', number_2)
