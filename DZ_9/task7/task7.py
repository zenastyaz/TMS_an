# Дан текстовый файл с несколькими строками.
# Зашифровать шифром Цезаря, при этом шаг зависит от
# номера строки: для первой строки шаг 1, для второй – 2 и т.д.
# Пример:
# Входные данные:         Выходные данные:
# Hello                   Ifmmp
# Hello                   Jgnnq
# Hello                   Khoor
# Hello                   Lipps


def user_input() -> int:

    print('Выберите действие:')
    print("1-Шифровать\n2-Дешифровать")
    vvod_2 = int(input())
    return vvod_2


def func_shi(text: str, vvod_2: int, shag: int) -> str:
    alfavit_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfavit_lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    itog = ''

    for i in text:
        if i.isupper():
            m = alfavit_upper.find(i)
            new_m = m + shag if vvod_2 == 1 else m - shag
            itog += alfavit_upper[new_m % 26]
        elif i.islower():
            m = alfavit_lower.find(i)
            new_m = m + shag if vvod_2 == 1 else m - shag
            itog += alfavit_lower[new_m % 26]
        else:
            itog += i

    return itog


def text_word(vvod_2: int):
    with open('file_1.txt', 'r') as file:
        text = file.readlines()
        number_line = 1
        for line in text:
            line_shi = func_shi(line.strip(), vvod_2, number_line)
            print("Сообщение для шифровки: ", line.strip())
            print("Зашифрованное сообщение: ", line_shi)
            number_line += 1


def main() -> None:
    vvod_2 = user_input()
    text_word(vvod_2)


main()
