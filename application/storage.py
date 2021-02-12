import json
from product import Product
from user import User


class OrderManager:
    data = [
        {"name": "Сърф", "price": 20, "quantity": 20},
        {"name": "Водно колело", "price": 15, "quantity": 20},
        {"name": "Хавлия", "price": 10, "quantity": 20},
        {"name": "Лодка", "price": 1200, "quantity": 20},
        {"name": "Водолазна маска", "price": 15, "quantity": 20},
        {"name": "Кислородна бутилка", "price": 60, "quantity": 20},
        {"name": "Плавници", "price": 30, "quantity": 20},
        {"name": "Шнорхел", "price": 15, "quantity": 20},
        {"name": "Вода", "price": 1, "quantity": 20},
        {"name": "Кола", "price": 1, "quantity": 20}

    ]

    def __init__(self):
        self.inventory = []
        self.basket = {}
        self.total_price = 0
        self.data_to_products()

    def data_to_products(self):
        for item in self.data:
            product = Product(item["name"], item["price"], item["quantity"])
            self.inventory.append(product)

    def list_products(self):
        for i in range(len(self.inventory)):
            print(f'{i}.{self.inventory[i]}')

    def add_item_basket(self, item_number, item_quantity):
        if self.inventory[item_number] and self.inventory[item_number].quantity > 0:
            if str(item_number) in self.basket:
                self.basket[str(item_number)].quantity += item_quantity
            else:
                product = self.inventory[item_number]
                product_in_basket = Product(product.name, product.price, item_quantity)
                self.basket[str(item_number)] = product_in_basket
                self.inventory[item_number].quantity -= item_quantity
        else:
            print("Недостатъчна наличност от избраният продукт")
        self.calculate_total_price()

    def list_basket(self):
        print("=======Вашата кошница===========")
        for key in self.basket:
            print(f'{self.basket[key]}')
        print(f' Крайна сума: {self.total_price}лв')

    def calculate_total_price(self):
        for item in self.basket:
            self.total_price += self.basket[item].price * self.basket[item].quantity

    def user_is_authorized(self, name, age, health):
        if age == int(age) and health in [x for x in range(1, 10)]:
            user = User(name, age, health)
            return user.is_eligible()
        else:
            print("Моля въведете коректни данни")
            return False
