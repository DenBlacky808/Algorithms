print("Введите длины трех отрезков ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Равносторонний")
    else:
        if a == c or a == b or b == c:
            print("Равнобедренный")
        else:
            print("Разносторонний")
else:
    print("Треугольник не существует")
