# Напишите программу, которая считывает текст из
# файла (в файле может быть больше одной строки) и выводит
# в новый файл самое часто встречаемое слово в каждой
# строке и число – счётчик количества повторений этого слова
# в строке.

def create_text():
    text = "Это пример текстового файла файла\nфайла пример файла"
    with open('file_1.txt', 'w') as file:
        file.write(text)


def texts():
    with open('file_1.txt', 'r') as file:
        text = file.readlines()

    with open('file_2', 'w') as file:
        for line in text:
            line = line.lower().split()
            word_c = {}
            for word in line:
                if word in word_c:
                    word_c[word] += 1
                else:
                    word_c[word] = 1
            max_count = 0
            for word, count in word_c.items():
                if count > max_count:
                    most_word = word
                    max_count = count
            result_line = f"Слово: {most_word} повторяется {max_count} раз\n"
            file.write(result_line)


create_text()
texts()
