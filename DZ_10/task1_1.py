import pymorphy2


class Soda:
    def __init__(self, flavor=None):
        self.flavor = flavor
        self.morph = pymorphy2.MorphAnalyzer()

    def __str__(self):
        if self.flavor:
            n_flavor = self.morph.parse(self.flavor)[0]
            new_flavor = n_flavor.inflect({'gent'}).word
            return f"У вас газировка со вкусом {new_flavor}"
        else:
            return "У вас обычная газировка"


soda1 = Soda("клубника")
soda2 = Soda()

print(soda1)
print(soda2)
