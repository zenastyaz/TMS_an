"""
Разработать класс SuperStr, который наследует
функциональность стандартного типа str и содержит два
новых метода:
● метод is_repeatance(s), который принимает некоторую
строку и возвращает True или False в зависимости от того,
может ли текущая строка быть получена целым
количеством повторов строки s. Считать, что пустая
строка не содержит повторов
● метод is_palindrom(), который возвращает True или False в
зависимости от того, является ли строка палиндромом вне
зависимости от регистра. Пустую строку считать
палиндромом.
"""


class SuperStr(str):
    def is_repeatance(self, s):
        if not s or len(self) % len(s) != 0:
            return False
        if self == s * (len(self) // len(s)):
            return True
        return False

    def is_palindrom(self):
        return self.lower() == self[::-1].lower()


s = SuperStr("abababab")
print(s.is_repeatance("ab"))
print(s.is_repeatance("abab"))
print(s.is_repeatance(""))
print(s.is_repeatance("a"))

p = SuperStr("Madam")
print(SuperStr("").is_palindrom())
