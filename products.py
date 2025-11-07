class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if price < 0:
            raise ValueError("Price must be non-negative.")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")

        self.name = name.strip()
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True

        if self.quantity == 0:
            self.deactivate()

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")
        self.quantity = int(quantity)
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")
        if quantity > self.quantity:
            raise ValueError(f"Not enough stock. Available: {self.quantity}")

        total = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return float(total)


#test:
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()