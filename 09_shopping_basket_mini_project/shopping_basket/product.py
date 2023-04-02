class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"product name {self.name} product price {self.price} product quantity {self.quantity}"


