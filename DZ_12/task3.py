"""
Паттерн «Строитель»
● Создайте класс Pizza, который содержит следующие
атрибуты: size, cheese, pepperoni, mushrooms, onions,
bacon.
● Создайте класс PizzaBuilder, который использует паттерн
«Строитель» для создания экземпляра Pizza. Этот класс
должен содержать методы для добавления каждого из
атрибутов Pizza.
● Создайте класс PizzaDirector, который принимает
экземпляр PizzaBuilder и содержит метод make_pizza,
который использует PizzaBuilder для создания Pizza.
"""


class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        list_ingredients = ['cheese', 'pepperoni', 'mushrooms', 'onions', 'bacon']
        ingredients = []
        for ingredient in list_ingredients:
            if getattr(self, ingredient):
                ingredients.append(ingredient)
        return f'Size {self.size},\nIngredients: {", ".join(ingredients) }'


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def make_pizza(self, size, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.builder.set_size(size)
        if cheese:
            self.builder.add_cheese()
        if pepperoni:
            self.builder.add_pepperoni()
        if mushrooms:
            self.builder.add_mushrooms()
        if onions:
            self.builder.add_onions()
        if bacon:
            self.builder.add_bacon()
        return self.builder.build()


builder = PizzaBuilder()
director = PizzaDirector()
director.builder = builder
pizza = director.make_pizza(size="Large", cheese=True, pepperoni=True, mushrooms=True)
print(pizza)
