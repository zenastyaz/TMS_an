"""
Реализовать программу для вывода
последовательности чисел Фибоначчи до определённого
числа в последовательности. Номер числа, до которого нужно
выводить, задаётся пользователем с клавиатуры. Для
реализации последовательности использовать генераторную
функцию.
"""


def fibonacci(n):
    a, b = 1, 1
    while a <= n:
        yield a
        a, b = b, a + b


num = int(input(": "))
for fib_num in fibonacci(num):
    print(fib_num)