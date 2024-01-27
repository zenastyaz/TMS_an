# В файл записано некоторое содержимое (буквы,
# цифры, пробелы, специальные символы и т.д.). Числом
# назовём последовательность цифр, идущих подряд. Вывести
# сумму всех чисел, записанных в файле.
# Пример:
# Входные данные: 123 ааа456 1x2y3z 4 5 6
# Выходные данные: 600


import re


def text_word() -> None:
    with open('file_1.txt', 'r') as file:
        text = file.read()
        print(text)
        num = re.findall(r'\d+', text)
        total_sum = sum(map(int, num))
        print(f"Сумма чисел: {total_sum}")


text_word()
