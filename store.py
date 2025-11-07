import products

class Store:
    def __init__(self, products: list):
        self.products = products

    def add_product(self, product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> list:
        """Returns all products in the store that are active."""
        all_products = []
        for product in self.products:
            if product.is_active():
                all_products.append(product)
        return all_products

    def order(self, shopping_list) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        total_price = 0
        for item in shopping_list:
            product, quantity = item
            price = product.buy(quantity)
            total_price += price
        return total_price


#test
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))