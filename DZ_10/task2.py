"""
Напишите программу с классом Math. При
инициализации атрибутов нет. Реализовать методы addition,
subtraction, multiplication и division. При передаче в методы
двух числовых параметров нужно производить с
параметрами соответствующие действия и печатать ответ
"""


class Math:
    def addition(self, a, b):
        result = a + b
        print(f"{a} + {b} = {result}")
        return result

    def subtraction(self, a, b):
        result = a - b
        print(f"{a} - {b} = {result}")
        return result

    def multiplication(self, a, b):
        result = a * b
        print(f"{a} * {b} = {result}")
        return result

    def division(self, a, b):
        if b == 0:
            print("Ошибка: Деление на ноль.")
            return None
        result = a * b
        print(f"{a} * {b} = {result}")
        return result


math = Math()

math.addition(10, 2)
math.subtraction(10, 2)
math.multiplication(10, 2)
math.division(10, 2)
math.division(10, 0)
