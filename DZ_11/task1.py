"""
Класс «Товар» содержит следующие закрытые поля:
● название товара
● название магазина, в котором подаётся товар
● стоимость товара в рублях
Класс «Склад» содержит закрытый массив товаров.
Обеспечить следующие возможности:
● вывод информации о товаре со склада по индексу
● вывод информации о товаре со склада по имени товара
● сортировка товаров по названию, по магазину и по цене
● перегруженная операция сложения товаров по цене
"""


class Product:
    def __init__(self, name_product, name_shop, prise):
        self.__name_product = name_product
        self.__name_shop = name_shop
        self.__prise = prise

    def __str__(self):
        return f"Товар: {self.__name_product}, Магазин: {self.__name_shop}, Цена: {self.__prise} руб."

    @property
    def get_name_product(self):
        return self.__name_product

    @property
    def get_name_shop(self):
        return self.__name_shop

    @property
    def get_prise(self):
        return self.__prise

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Объект для сложения должен быть инстансом класса Product")
        sum_price = self.get_prise + other.get_prise
        return sum_price


class Stock:
    def __init__(self, *products):
        self.__products = []
        for product in products:
            if not isinstance(product, Product):
                raise TypeError
            self.__products.append(product)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)

    def __getitem__(self, key):
        if isinstance(key, int):
            if 0 <= key < len(self.__products):
                return self.__products[key]
            else:
                raise IndexError("Товар с таким индексом не найден.")
        elif isinstance(key, str):
            for product in self.__products:
                if product.get_name_product == key:
                    return product
            raise ValueError("Товар с таким названием не найден.")
        else:
            raise TypeError("Ключ должен быть целым числом или строкой.")

    def sort(self, by='name'):
        if by == 'name':
            self.__products.sort(key=lambda x: x.get_name_product)
        elif by == 'shop':
            self.__products.sort(key=lambda x: x.get_name_shop)
        elif by == 'prise':
            self.__products.sort(key=lambda x: x.get_prise)


def main():
    products = [
        Product("iPhone 13", "i-store", 1100),
        Product("Samsung Galaxy S21", "21vek", 1000),
        Product("Xiaomi Redmi Note 10", "Связной", 900)
    ]
    stock = Stock(*products)

    while True:
        print("Выберите действие: ")
        num = int(input("1.Добавить товар\n2.Вывести товар по индексу\n3.Вывести товар по названию\n"
                        "4.Сортировать товар\n5.Сложить стоимость 2х товаров\n6.Выйти.\n"))
        if num == 1:
            name_p = input("Введите название товара: ")
            name_s = input("Введите название магазина: ")
            prise = input("Введите стоимость товара: ")
            stock.add_product(Product(name_p, name_s, prise))
            print(f"Товар {name_p} добавлен.")

        elif num == 2:
            try:
                index = int(input("Введите индекс товара: "))
                print(stock[index])
            except IndexError as e:
                print(e)
        elif num == 3:
            name = input("Введите название товара: ")
            try:
                product = stock[name]
                print(product)
            except ValueError as e:
                print(e)

        elif num == 4:
            sort = input("Сортировать товар по:\n1. Названию\n2. Магазину\n3. Цене\n ")
            if sort == 1:
                stock.sort('name')
            elif sort == 2:
                stock.sort('shop')
            elif sort == 3:
                stock.sort('prise')

        elif num == 5:
            prod1 = input("Введите название первого товара: ")
            prod2 = input("Введите название первого товара: ")
            try:
                product1 = stock[prod1]
                product2 = stock[prod2]
                sum_price = product1 + product2
                print(f"Общая стоимость 2х товаров: {sum_price} руб.")
            except (ValueError, TypeError) as e:
                print(e)

        elif num == 6:
            break


main()

# Product("iPhone 13", "i-store", 1100),
# Product("Samsung Galaxy S21", "21vek", 1000),
# Product("Xiaomi Redmi Note 10", "Связной", 900)
# "Huawei P30", "21vek", 850)
