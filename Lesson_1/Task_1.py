"""

https://drive.google.com/file/d/1aN5F58ElVzOpvGbyOQE5uCr58Hitiy6k/view?usp=sharing

"""

number = int(input('Введите трехзначное число '))
hundr = number // 100
tens = (number - hundr * 100) // 10
single = number - hundr * 100 - tens * 10
print(hundr + tens + single, hundr * tens * single)
