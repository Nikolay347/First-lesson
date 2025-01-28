# Internet shop
class Item:

    def __init__(self, name, price, description, dimensions):
        # Initiation by attributes of the class Item object. Instance attributes.
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        # Defining a custom string representation of an object.
        return f"{self.name}, price: {self.price}, description: {self.description}, dimension: {self.dimensions}"
##
class User:

    def __init__(self, name, surname, numberphone):
        # Initiation by attributes of the class User object. Instance attributes.
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        # Defining a custom string representation of an object.
        return f"{self.name.title()} {self.surname.title()}"


class Purchase:
    def __init__(self, user):
        # Initiation by attributes of the class Purchase object. Instance attributes.
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        #Function for determining the quantity of the product
        self.products[item] = cnt

    def __str__(self):
        # Defining a custom string representation of an object.
        all_products = ""
        for product, count in self.products.items():
            all_products += f"\n{product.name}: {count} pcs."
        return f"User: {self.user}\nItems:{all_products}"

    # """
    # User: Ivan Ivanov
    # Items:
    # lemon: 4 pcs.
    # apple: 20 pcs.
    # """
    def get_total(self):
        #The function for the final count of purchases
        all_sum = 0
        for product, count in self.products.items():
            all_sum += (product.price * count)
        return all_sum
# Entering purchase data:
buyer_1 = User("Tim", "Markovich", "+348746448441")
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

cart = Purchase(buyer_1)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
print()


assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'


cart.add_item(apple, 10)        #Changes in buying apples. Changing the entire purchase
print(cart)
assert cart.get_total() == 40
