# Напишите программу, которая получает на вход строку
# с названием текстового файла и выводит на экран
# содержимое этого файла, заменяя все запрещённые слова
# звездочками. Запрещённые слова, разделённые символом
# пробела, должны храниться в файле stop_words.txt.
# Программа должна находить
# запрещённые слова в любом месте файла, даже в середине
# другого слова. Замена независима от регистра: если в списке
# запрещённых есть слово exam, то замениться должны exam,
# eXam, EXAm и другие вариации.
# Пример: в stop_words.txt записаны слова: hello email
# python the exam wor is
# Текст файла для цензуры выглядит так: Hello, World! Python
# IS the programming language of thE future. My EMAIL is...
# PYTHON as AwESOME!
# Тогда итоговый текст: *****, ***ld! ****** ** *** programming
# language of *** future. My ***** **... ****** ** awesome!!!


def stop_word(file_path):
    with open(file_path, 'r') as file:
        stop_w = file.read().split()
    return stop_w


def texts(file_path, stop_w):
    with open(file_path, 'r') as file:
        content = file.read().lower()
    for word in stop_w:
        content = content.replace(word, '*' * len(word))
    return content


stop_words = stop_word('stop_words.txt')
text = 'words.txt'
filtered_text = texts(text, stop_words)

print(filtered_text)
