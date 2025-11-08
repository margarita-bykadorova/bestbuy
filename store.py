class Store:
    """
    Represents a store that holds and manages a collection of products.
    """

    def __init__(self, products):
        """
        Initialize a new Store.
        """
        self.products = products


    def add_product(self, product):
        """
        Add a product to the store.
        """
        self.products.append(product)


    def remove_product(self, product):
        """
        Remove a product from the store.
        """
        self.products.remove(product)


    def get_total_quantity(self):
        """
        Return the total number of items in the store (int).
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self):
        """
        Return a list of all active products in the store.
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        """
        Buy multiple products and return the total cost (float).
        """
        total_price = 0

        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError("Product not in store")
            total_price += product.buy(quantity)

        return total_price
