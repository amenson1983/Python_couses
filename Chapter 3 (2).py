a1 = float(input("Введите длину первого прямоугольника: "))
b1 = float(input("Введите ширину первого прямоугольника: "))
a2 = float(input("Введите длину второго прямоугольника: "))
b2 = float(input("Введите ширину второго прямоугольника: "))
c1 = a1*b1
c2 = a2*b2
if c1 > c2:
    print("Площадь первого прямоугольника больше, чем второго")
elif c1==c2:
    print("Площади прямоугольников равны")
else:
    print("Площадь второго прямоугольника больше, чем первого")