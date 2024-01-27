# Реализовать программу с функционалом калькулятора для операций над двумя числами.
# Числа и операция вводятся пользователем с клавиатуры.
# Использовать обработку исключений.

def user_input(a, b, zh):
    if not a <= 1000:
        raise Exception("Произошла ошибка при вводе")
    if not b <= 1000:
        raise Exception("Произошла ошибка при вводе")
    if zh not in ['+', '-', '*', '/']:
        raise Exception("Неверная операция. Пожалуйста, выберите +, -, *, /")


def calculate(zh, a, b):
    if zh == '+':
        result = a + b
    elif zh == '-':
        result = a - b
    elif zh == '*':
        result = a * b
    elif zh == '/':
        if a == 0 or b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        result = a / b
    else:
        raise ValueError("Некорректная операция")
    return result


def run_calculate():
    while 1:
        try:
            s = float(input('Введите число: '))
            d = float(input('Введите число: '))
            zn = input("Выберите операцию (+, -, *, /) ")
            user_input(s, d, zn)
            c_result = calculate(zn, s, d)
            print("Результат:", c_result)
            break
        except ValueError:
            print("Введены некорректные данные")
        except Exception as e:
            print(e)


run_calculate()
