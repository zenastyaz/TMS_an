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

    def info(self):
        return f"Товар: {self.__name_product}, Магазин: {self.__name_shop}, Цена: {self.__prise} руб."

    def get_name_product(self):
        return self.__name_product

    def get_name_shop(self):
        return self.__name_shop

    def get_prise(self):
        return self.__prise

    def __add__(self, other):
        if isinstance(other, Product):
            sum_price = self.get_prise() + other.get_prise()
            return sum_price


class Stock:
    def __init__(self):
        self.__products = [
            Product("iPhone 13", "i-store", 1100),
            Product("Samsung Galaxy S21", "21vek", 1000),
            Product("Xiaomi Redmi Note 10", "Связной", 900)
        ]

    def add_product(self, product):
        self.__products.append(product)

    def get_product_index(self, index):
        if 0 <= index < len(self.__products):
            return self.__products[index].info()
        else:
            return "Товар с таким индексом не найден."

    def get_name_product_(self, name_p):
        for product in self.__products:
            if product.get_name_product() == name_p:
                return product
        return "Товар с таким названием не найден."

    def sort_products(self, by='name'):
        if by == 'name':
            self.__products.sort(key=lambda x: x.get_name_product())
        elif by == 'shop':
            self.__products.sort(key=lambda x: x.get_name_shop())
        elif by == 'prise':
            self.__products.sort(key=lambda x: x.get_prise())


def main():
    stock = Stock()
    while True:
        print("Выберите действие: ")
        num = int(input("1.Добавить товар\n2.Вывести товар по индексу\n3.Вывести товар по названию\n"
                        "4.Сортировать товар\n5.Сложить стоимость 2х товаров\n6.Выйти.\n"))
        if num == 1:
            name_p = input("Введите название товара: ")
            name_s = input("Введите название магазина: ")
            prise = input("Введите стоимость товара: ")
            stock.add_product(Product(name_p, name_s, prise))
        elif num == 2:
            index = int(input("Введите индекс товара: "))
            print(stock.get_product_index(index))
        elif num == 3:
            name = input("Введите название товара: ")
            product = stock.get_name_product_(name)
            if product:
                print(product.info())
        elif num == 4:
            sort = input("Сортировать товар:\n1.ПО названию товара\n2.По магазину\n3.По стоимости\n")
            if sort == 1:
                stock.sort_products('name')
            elif sort == 2:
                stock.sort_products('shop')
            elif sort == 3:
                stock.sort_products('prise')
        elif num == 5:
            prod1 = input("Введите название первого товара: ")
            prod2 = input("Введите название первого товара: ")
            product1 = stock.get_name_product_(prod1)
            product2 = stock.get_name_product_(prod2)
            sum_price = product1 + product2
            print(f"Общая стоимость 2х товаров: {sum_price} руб.")
        elif num == 6:
            break


main()


# "Huawei P30", "21vek", 850)

