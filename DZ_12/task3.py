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
    def __init__(self, size=None):
        self.size = size
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
        built_pizza = self.pizza
        self.pizza = Pizza(self.pizza.size)
        return built_pizza


class PizzaDirector:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def make_pepperoni_pizza(self):
        return self._builder.set_size("Large").add_cheese().add_pepperoni().build()

    def make_veggie_pizza(self):
        return self._builder.set_size("Medium").add_cheese().add_mushrooms().add_onions().build()


builder = PizzaBuilder()
director = PizzaDirector()
director.builder = builder
pepperoni_pizza = director.make_pepperoni_pizza()
veggie_pizza = director.make_veggie_pizza()

print(pepperoni_pizza)
print(veggie_pizza)
