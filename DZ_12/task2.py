"""
Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2...).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся
пользователем с клавиатуры.
"""


def func(nums):
    while True:
        for n in nums:
            yield n


user_input = input("Введите последовательность чисел: ")
nums = []
for n in user_input.split():
    num = int(n)
    nums.append(num)
num = int(input(": "))
f = func(nums)
for _ in range(num):
    print(next(f), end="-")
