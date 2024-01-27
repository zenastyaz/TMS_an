"""
Класс «Автобус». Класс содержит свойства:
● скорость
● максимальное количество посадочных мест
● максимальная скорость
● список фамилий пассажиров
● флаг наличия свободных мест
● словарь мест в автобусе
Методы:
● посадка и высадка одного или нескольких пассажиров
● увеличение и уменьшение скорости на заданное значение
● операции in, += и -= (посадка и высадка пассажира по
фамилии)
"""


class Bus:
    def __init__(self, speed, max_seats, max_speed):
        self.speed = speed
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passenger_list = []
        self.seat_map = {}

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_max_seats(self):
        return self.max_seats

    def get_max_speed(self):
        return self.max_speed

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    def get_passenger_list(self):
        return self.passenger_list

    def set_passenger_list(self, passenger_list):
        self.passenger_list = list(passenger_list)

    def get_free_seats(self):
        return self.max_seats - len(self.seat_map)

    def board_passengers(self, passenger_list):
        free_seats = self.get_free_seats()
        for passenger in passenger_list:
            if free_seats > 0:
                if passenger not in self.passenger_list:
                    self.passenger_list.append(passenger)
                    free_seats -= 1
                    print(f"Добавлен пасажир {passenger}")
            else:
                return "В автобусе нет свободных мест"

    def __iadd__(self, passenger):
        self.board_passengers([passenger])
        return self

    def alight_passengers(self, passenger):
        free_seats = self.get_free_seats()
        if passenger in self.passenger_list:
            self.passenger_list.remove(passenger)
            free_seats += 1
            print(f"Высадили пасажира с фимилией: {passenger}")
        else:
            return "В автобусе нет пасажира с такой фамилией"

    def __isub__(self, passenger):
        self.alight_passengers(passenger)
        return self

    def __contains__(self, passenger):
        return passenger in self.passenger_list

    def change_speed(self, speed_change):
        if self.speed + speed_change < self.max_speed:
            self.speed += speed_change
            return f"Скорость изменена на {self.speed}"
        else:
            return "Нельзя увелиличивать скорость"


b = Bus(60, 10, 120)
b.passenger_list = (["Иванов", "Петров", "Сидоров"])
print(b.speed)
print(b.max_seats)
print(b.max_speed)
print(b.get_passenger_list())
print(b.get_free_seats())

print(b.board_passengers(["Алексеева", "Кузнецов"]))
b += "Михайлов"
print(b.get_passenger_list())

b.alight_passengers("Сидоров")
b -= "Иванов"
print(b.get_passenger_list())

print("Петров" in b)
print(b.change_speed(30))
