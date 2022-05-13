# NUM 12
import math
print("Введите радиус и высоту цилиндра")
r = int(input("Радиус: "))
h = int(input("Высота: "))
v = float(math.pi * (r ** 2) * h)
v = ("{:.1f}".format(v))
print("Объем шара равен: ", v)
