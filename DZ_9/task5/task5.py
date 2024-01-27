# В текстовый файл построчно записаны фамилия и имя
# учащихся класса и оценка за контрольную. Вывести на экран
# всех учащихся, чья оценка меньше трёх баллов.


def read_grades() -> None:
    with open('grades.txt', 'r') as file:
        for line in file:
            surname, name, grade = line.strip().split()
            grade = int(grade)
            if grade < 3:
                print(f"{surname} {name} - Оценка: {grade}")


read_grades()
