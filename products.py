class Product:
    """
    Represents a product in the store, including its name, price,
    quantity in stock, and active status.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize a new Product.
        Raise a ValueError if name is empty or price/quantity are negative.
        """
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


    def get_quantity(self):
        """
        Return the current stock quantity.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Update the stock quantity.
        Deactivates the product automatically if quantity becomes 0.
        Raise ValueError if quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")
        self.quantity = int(quantity)
        if self.quantity == 0:
            self.deactivate()


    def is_active(self):
        """
        Return True if the product is active, otherwise False.
        """
        return self.active


    def activate(self):
        """
        Activate the product.
        """
        self.active = True


    def deactivate(self):
        """
        Deactivate the product.
        """
        self.active = False


    def show(self):
        """
        Print a formatted description of the product.
        """
        print(f"{self.name}, Price: ${self.price:g}, Quantity: {self.quantity}")


    def buy(self, quantity):
        """
        Purchase a given quantity of the product.
        Return the total price of the purchase.
        Raise Exception if the product is inactive.
        Raise ValueError if quantity is invalid or exceeds stock.
        """
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")
        if quantity > self.quantity:
            raise ValueError(f"Not enough stock. Available: {self.quantity}")

        total = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return float(total)
