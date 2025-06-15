class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name.title()} {self.surname.title()}"


class Purchase:
    def __init__(self, user):
        self.products = {}  # словник: товар -> кількість
        self.user = user

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        all_products = ""
        for product, count in self.products.items():
            all_products += f"\n{product.name}: {count} pcs."
        return f"User: {self.user}\nItems:{all_products}"

    def get_total(self):
        total = 0
        for product, count in self.products.items():
            total += product.price * count
        return total

lemon = Item('lemon', 5, "yellow citrus", "small")
apple = Item('apple', 2, "red apple", "medium")


