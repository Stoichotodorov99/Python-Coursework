class Product:
    name = 'default'
    price = 0
    quantity = 0

    def __init__(self, name,price,quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name} - {self.price}лв. - {self.quantity} броя '
