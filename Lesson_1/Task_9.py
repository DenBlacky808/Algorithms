print("Введите три разных числа ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a > b:
    if a < c:
        print(a)
    else:
        print(b)
else:
    if b < c:
        print(b)
    else:
        print(c)
