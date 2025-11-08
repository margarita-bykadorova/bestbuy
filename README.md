# Store Management CLI

A simple command-line application for browsing products, checking stock,
and placing orders.  
Built as an introduction to Object-Oriented Programming in Python.

---

## Features

✅ Product class  
✅ Store class  
✅ Track quantity & activation status  
✅ Prevent purchases of inactive or out-of-stock products  
✅ User-friendly CLI menu  
✅ Clean, modular structure (PEP 8)  

---

## Project Structure

```
project/
├── products.py   # Product class
├── store.py      # Store class
└── main.py       # CLI program (entry point)
```

---

## Usage

### Run the program

```
python main.py
```

---

## How It Works

### Main Menu

```
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
```

Choose an option by entering `1–4`.

---

## Product

Each product has:

- name
- price
- quantity in stock
- active/inactive status

When quantity reaches `0`, the product becomes inactive automatically.

Key methods:

- `show()`
- `buy(quantity)`
- `get_quantity()`
- `set_quantity(quantity)`
- `is_active()`

---

## Store

The store manages a list of products. It supports:

- Adding products
- Removing products
- Retrieving all **active** products
- Buying multiple products at once via `order()`

---

## Example

```python
from products import Product
from store import Store

# Create products
mac = Product("MacBook Air M2", price=1450, quantity=100)
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)

# Create store
best_buy = Store([mac, bose])

# Order
total = best_buy.order([(mac, 2), (bose, 3)])
print(total)   # Cost of the order
```

---

## Error Handling

The program raises exceptions for:

- Invalid product name
- Negative price or quantity
- Purchasing more than available
- Purchasing from inactive products
- Invalid menu input

---

## Extending the Project

Possible enhancements:

- Support for discounts
- Persistent storage (files/DB)
- Automated tests
- Admin/user modes
- Data import/export

---

## Requirements

- Python 3.8+

No external libraries required.

---

## Author

**margarita-bykadorova**  
[GitHub Profile](https://github.com/margarita-bykadorova)
