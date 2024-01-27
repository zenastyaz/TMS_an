"""
Программа с классом Car. При инициализации объекта
ему должны задаваться атрибуты color, type и year.
Реализовать пять методов. Запуск автомобиля – выводит
строку «Автомобиль заведён». Отключение автомобиля –
выводит строку «Автомобиль заглушен». Методы для
присвоения автомобилю года выпуска, типа и цвета.
"""


class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_car(self):
        print("Автомобиль заведён")

    def stop_car(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color


car = Car("Красный", "Седан", 2020)
car.start_car()
car.set_year(2021)
car.set_type("Хэтчбек")
car.set_color("Синий")
car.stop_car()
