"""
ПчёлоСлон
Экземпляр класса инициализируется двумя целыми числами,
первое относится к пчеле, второе – к слону. Класс реализует
следующие методы:
● fly() – возвращает True, если часть пчелы не меньше части
слона, иначе – False
● trumpet() – если часть слона не меньше части пчелы,
возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
● eat(meal, value) – может принимать в meal только ”nectar”
или “grass”. Если съедает нектар, то value вычитается из
части слона, пчеле добавляется. Иначе – наоборот. Не
может увеличиваться больше 100 и уменьшаться меньше 0.
"""


class BeeElephant:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return False

    def trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elephant -= value
            if self.elephant < 0:
                self.elephant = 0
            self.bee += value
            if self.bee > 100:
                self.bee = 100
        elif meal == "grass":
            self.bee -= value
            if self.bee < 0:
                self.bee = 0
            self.elephant += value
            if self. elephant > 100:
                self.elephant = 100
        return self.bee, self.elephant


b = BeeElephant(20, 10)
print(b.fly())
print(b.trumpet())
print(b.eat("nectar", 5))
print(b.eat("grass", 15))
