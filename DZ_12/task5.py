"""
Паттерн «Стратегия»
● Создайте класс Calculator, который использует разные
стратегии для выполнения математических операций.
● Создайте несколько классов, каждый реализует
определенную стратегию математической операции,
например, Addition, Subtraction, Multiplication, Division.
Каждый класс должен содержать метод execute, который
принимает два числа и выполняет соответствующую
операцию.
● Calculator должен иметь метод set_strategy, который
устанавливает текущую стратегию, и метод calculate,
который выполняет операцию с помощью текущей стратегии.
"""


from abc import ABC, abstractmethod


class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        if not isinstance(a, (int, float)):
            return
        return self.strategy.execute(a, b)


class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(Strategy):
    def execute(self, a, b):
        return a + b


class Subtraction(Strategy):
    def execute(self, a, b):
        return a - b


class Multiplication(Strategy):
    def execute(self, a, b):
        return a * b


class Division(Strategy):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero!")
        return a / b


c = Calculator(Addition())
print(c.calculate(2, 3))
c.set_strategy(Multiplication())
print(c.calculate(2, 3))
