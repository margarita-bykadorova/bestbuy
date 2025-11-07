import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start():
    while True:
        print("\nStore Menu")
        print("-" * 10)
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = get_valid_choice()
        handle_choice(choice)

def get_valid_choice():
    """Get an integer from 1 to 4."""
    while True:
        try:
            choice = int(input("Please choose a number: "))
            if 0 < choice < 5:
                return choice
            else:
                print("Please enter a number from 1 to 4.")
        except ValueError:
            print("Wrong input! Please enter an integer.")


def make_order():
    active = show_products()
    print("When you want to finish order, enter empty text.")
    shopping_list = []

    while True:
        prod_inp = input("Which product # do you want? ").strip()
        if prod_inp == "":
            break
        if not prod_inp.isdigit():
            print("Please enter a valid product number.")
            continue

        idx = int(prod_inp)
        if not (1 <= idx <= len(active)):
            print("No such product number.")
            continue

        qty_inp = input("What amount do you want? ").strip()
        if qty_inp == "":
            print("Please enter a quantity.")
            continue
        if not qty_inp.isdigit():
            print("Quantity must be a positive integer.")
            continue

        qty = int(qty_inp)
        product = active[idx - 1]

        if not product.is_active():
            print("That product is not active.")
            continue
        if qty <= 0:
            print("Quantity must be positive.")
            continue
        if qty > product.get_quantity():
            print(f"Not enough stock. Available: {product.get_quantity()}")
            continue

        shopping_list.append((product, qty))
        print("Product added to list!")

    if not shopping_list:
        print("No items selected.")
        return

    try:
        total = best_buy.order(shopping_list)
        print("********")
        print(f"Order made! Total payment: ${total}")
    except Exception as e:
        print(f"Order failed: {e}")


def show_products():
    """Prints and returns all active products from the store"""
    active = best_buy.get_all_products()
    print("-" * 6)
    for idx, p in enumerate(active, start=1):
        print(f"{idx}. {p.name}, Price: ${p.price}, Quantity: {p.get_quantity()}")
    print("-" * 6)
    return active


def handle_choice(choice):
    if choice == 1:
        show_products()
    elif choice == 2:
        print(f"Total of {best_buy.get_total_quantity()} items in store")
    elif choice == 3:
        make_order()
    elif choice == 4:
        exit()

