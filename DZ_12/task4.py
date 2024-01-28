"""
Паттерн «Фабричный метод»
● Создайте абстрактный класс Animal, у которого есть
абстрактный метод speak.
● Создайте классы Dog и Cat, которые наследуют от Animal
и реализуют метод speak.
● Создайте класс AnimalFactory, который использует
паттерн «Фабричный метод» для создания экземпляра
Animal. Этот класс должен иметь метод create_animal,
который принимает строку («dog» или «cat») и возвращает
соответствующий объект (Dog или Cat).
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Dog"


class Cat(Animal):
    def speak(self):
        return "Cat"


class AnimalFactory:
    def create_animal(self, animal):
        if animal == 'dog':
            return Dog()
        elif animal == 'cat':
            return Cat()
        else:
            return "Unknown animal type"


f = AnimalFactory()
dog = f.create_animal("dog")
print(dog.speak())

cat = f.create_animal("cat")
print(cat.speak())
