"""
Программа с классом Sphere для представления сферы в трёхмерном пространстве. Реализовать методы:
● конструктор, принимающий 4 числа: радиус и координаты центра сферы x, y, z. Если конструктор вызывается без
аргументов, создать объект сферы с единичным радиусом и центром в начале координат. Если конструктор
вызывается только с радиусом, создать объект с соответствующим радиусом и центром в начале координат
● метод get_volume(), возвращающий число – объем шара, ограниченного текущей сферой
● метод get_square(), возвращающий число – площадь внешней поверхности сферы
● метод get_radius(), возвращающий число – радиус текущей сферы
● метод get_center(), возвращающий кортеж с координатами центра сферы
● метод set_radius(radius), который принимает новое значение радиуса, меняет радиус текущей сферы и ничего
не возвращает
● метод set_center(x, y, z), который принимает новые значения для координат центра радиуса, меняет
координаты текущей сферы и ничего не возвращает
● метод is_point_inside(x, y, z), который принимает координаты некой точки в трёхмерном пространстве и
возвращает True или False в зависимости от того, находится ли точка внутри сферы
"""


import math


class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        return (self.center[0] - x) ** 2 + (self.center[1] - y) ** 2 + (self.center[2] - z) ** 2 < self.radius ** 2


sphere = Sphere()
print("Объем:", sphere.get_volume())
print("Площадь поверхности:", sphere.get_square())

sphere.set_radius(3)
sphere.set_center(1, 1, 1)
print("Новый радиус:", sphere.get_radius())
print("Новый центр:", sphere.get_center())
print("Точка (2, 2, 2) внутри сферы:", sphere.is_point_inside(2, 2, 2))
print("Точка (4, 2, 2) не внутри сферы:", sphere.is_point_inside(4, 2, 2))
