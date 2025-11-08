import sys
from products import Product
from store import Store


MENU = (
    "\n   Store Menu\n"
    "   ----------\n"
    "1. List all products in store\n"
    "2. Show total amount in store\n"
    "3. Make an order\n"
    "4. Quit\n"
)


def print_menu():
    """
    Print the main menu.
    """
    print(MENU, end="")


def get_menu_choice():
    """
    Prompt the user for a menu choice (1–4) and return it.
    """
    while True:
        try:
            choice = int(input("Please choose a number: "))
        except ValueError:
            print("Wrong input! Please enter an integer.")
            continue

        if 1 <= choice <= 4:
            return choice

        print("Please enter a number from 1 to 4.")


def show_products(store):
    """
    Print active products with indices and return the list that was shown.
    """
    active = store.get_all_products()

    print("------")
    for index, product in enumerate(active, start=1):
        print(
            f"{index}. {product.name}, Price: ${product.price}, "
            f"Quantity: {product.get_quantity()}"
        )
    print("------")

    return active


def ask_for_product(active):
    """
    Prompt for a product index.
    Returns the Product or None (finish order).
    """
    raw = input("Which product # do you want? ").strip()

    if raw == "":
        return None

    if not raw.isdigit():
        print("Please enter a valid product number.")
        return ask_for_product(active)

    index = int(raw)
    if index < 1 or index > len(active):
        print("No such product number.")
        return ask_for_product(active)

    return active[index - 1]


def ask_for_quantity(product):
    """
    Prompt for a positive quantity within stock.
    """
    while True:
        raw = input("What amount do you want? ").strip()

        if not raw.isdigit():
            print("Quantity must be a positive integer.")
            continue

        quantity = int(raw)

        if quantity <= 0:
            print("Quantity must be positive.")
            continue

        available = product.get_quantity()
        if quantity > available:
            print(f"Not enough stock. Available: {available}")
            continue

        return quantity


def collect_items(active):
    """
    Interactively build a shopping list of (product, quantity).
    """
    print("When you want to finish order, enter empty text.")
    items = []

    while True:
        product = ask_for_product(active)
        if product is None:
            break

        if not product.is_active():
            print("That product is not active.")
            continue

        quantity = ask_for_quantity(product)

        items.append((product, quantity))
        print("Product added to list!")

    return items


def make_order(store):
    """
    Complete ordering flow: display, collect selections, place order.
    """
    active = show_products(store)
    shopping_list = collect_items(active)

    if not shopping_list:
        print("No items selected.")
        return

    try:
        total = store.order(shopping_list)
    except ValueError as error:
        print(f"Order failed: {error}")
        return

    print("********")
    print(f"Order made! Total payment: ${total}")


def handle_choice(choice, store):
    """
    Execute the selected menu choice.
    Returns False to quit; True to continue.
    """
    if choice == 1:
        show_products(store)
    elif choice == 2:
        print(f"Total of {store.get_total_quantity()} items in store")
    elif choice == 3:
        make_order(store)
    elif choice == 4:
        return False

    return True


def build_default_store():
    """
    Create a Store with the initial inventory.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    return Store(product_list)


def main():
    """
    Program entry point.
    """
    store = build_default_store()

    while True:
        print_menu()
        choice = get_menu_choice()
        should_continue = handle_choice(choice, store)

        if not should_continue:
            sys.exit(0)


if __name__ == "__main__":
    main()
