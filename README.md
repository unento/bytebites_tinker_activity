# ByteBites

Backend logic for ByteBites, a campus food ordering app, built with plain Python classes. This is a CodePath Week 3 tinker activity: turn a client feature request into a UML design, then implement and test it.

## What it does

- **Customers** have a name and a purchase history of past orders.
- **Food items** have a name, price, category and popularity rating.
- **The menu** holds every item and can filter by category (case-insensitive).
- **Orders** group the items a customer picks and compute the total cost.

## Classes

| Class | Attributes | Methods |
|---|---|---|
| `FoodItem` | `name`, `price`, `category`, `popularity_rating` | none |
| `Menu` | `items` | `add_item(item)`, `filter_by_category(category)` |
| `Order` | `items` | `add_item(item)`, `compute_total()` |
| `Customer` | `name`, `purchase_history` | `add_order(order)` |

A customer links to its orders through `purchase_history`, but an order does not store its customer. To order two of the same item, add it twice. An empty order totals `0.0`.

The full diagram and design rationale are in [bytebites_design.md](bytebites_design.md).

## Example

```python
from models import FoodItem, Menu, Order, Customer

burger = FoodItem("Spicy Burger", 8.99, "Food", 4.5)
soda = FoodItem("Large Soda", 2.49, "Drinks", 4.0)

menu = Menu()
menu.add_item(burger)
menu.add_item(soda)
menu.filter_by_category("drinks")  # [soda]

order = Order()
order.add_item(burger)
order.add_item(soda)
order.compute_total()  # 11.48

customer = Customer("Alice")
customer.add_order(order)
```

## Setup and testing

Requires Python 3.9 or newer.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pytest -v
```

On macOS or Linux, activate with `source .venv/bin/activate` instead.

## Project files

| File | Purpose |
|---|---|
| [models.py](models.py) | The four classes |
| [test_bytebites.py](test_bytebites.py) | pytest suite (13 tests) |
| [bytebites_spec.md](bytebites_spec.md) | Original client feature request |
| [bytebites_uml.md](bytebites_uml.md) | First draft of the UML diagram |
| [bytebites_design.md](bytebites_design.md) | Revised UML diagram, traceability table and design notes |
| [ByteBites_Design_Reference.md](ByteBites_Design_Reference.md) | Scope and style rules for the project |

## Out of scope

Authentication, a database, AI recommendations, and customer verification are not implemented. The spec says purchase history exists "so the system can verify they are real users" but doesn't define a rule, so that's left as an open question in the design.
