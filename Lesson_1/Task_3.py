print("Введите координаты двух точек по порядку (x1, y1, x2, y2):")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(" y = %.2f*x + %.2f" % (k, b))
