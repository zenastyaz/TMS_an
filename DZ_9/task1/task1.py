# Есть папка, в которой лежат файлы с разными расширениями.
# Программа должна:
# ● Вывести имя вашей ОС
# ● Вывести путь до папки, в которой вы находитесь
# ● Рассортировать файлы по расширениям, например, для
# текстовых файлов создается папка, в неё перемещаются
# все файлы с расширением .txt, то же самое для остальных
# расширений
# ● После рассортировки выводится сообщение типа «в папке
# с текстовыми файлами перемещено 5 файлов, их
# суммарный размер - 50 гигабайт»
# ● Как минимум один файл в любой из получившихся
# поддиректорий переименовать. Сделать вывод
# сообщения типа «Файл data.txt был переименован в
# some_data.txt»
# ● Программа должна быть кроссплатформенной – никаких
# хардкодов с именем диска и слэшами.


import os


def main():
    os_name = os.name
    if os_name == 'posix':
        print("Операционная система: MacOS")
    else:
        print("Операционная система: ", os.name)
    print("Текущий путь: ", os.getcwd())

    file_1 = 'file_1.txt'
    file_2 = 'file_2.txt'
    file_3 = 'file_3.docx'
    file_4 = 'file_4.docx'

    with open(file_1, 'w') as file:
        file.write("Это пример текстового файла.")
    with open(file_2, 'w') as file:
        file.write("Это пример текстового файла.")
    with open(file_3, 'w') as file:
        file.write("Привет, это документ Word!")
    with open(file_4, 'w') as file:
        file.write("Привет, это документ Word!")

    files = os.listdir(os.getcwd())
    print("Все файлы из директории:", files)

    file_o = []
    for f in files:
        if os.path.isfile(f):
            file_o = os.path.splitext(f)

    for f in file_o:
        n_file = os.path.splitext(f)[1][1:]
        if n_file:
            new_file = n_file + '_files'
            if not os.path.exists(new_file):
                os.makedirs(new_file)
            os.rename(f, os.path.join(new_file, f))

    for d in os.listdir('.'):
        if os.path.isdir(d):
            dir_files = os.listdir(d)
            size = 0
            for f in dir_files:
                file_p = os.path.join(d, f)
                size += os.path.getsize(file_p)
            print(f"В папке {d} перемещено {len(dir_files)} файлов, их суммарный размер - {size} байт")

    path = 'task1/txt_files'
    old_name = 'file_1.txt'
    new_name = 'renamed_' + old_name
    old_path = os.path.join(path, old_name)
    new_path = os.path.join(path, new_name)
    os.rename(old_path, new_path)
    print(f"Файл {old_name} был переименован в {new_name}")


main()
