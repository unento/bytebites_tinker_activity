"""ByteBites backend models: Customer, FoodItem, Menu, Order."""


class FoodItem:
    """A single item for sale, e.g. "Spicy Burger" or "Large Soda"."""

    def __init__(self, name: str, price: float, category: str, popularity_rating: float) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def __repr__(self) -> str:
        return f"FoodItem({self.name!r}, {self.price}, {self.category!r}, {self.popularity_rating})"


class Menu:
    """The full collection of food items, filterable by category."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        self.items.append(item)

    def filter_by_category(self, category: str) -> list[FoodItem]:
        """Return items whose category matches, ignoring case."""
        return [item for item in self.items if item.category.lower() == category.lower()]


class Order:
    """A single transaction grouping the items a customer picked."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        self.items.append(item)

    def compute_total(self) -> float:
        return sum((item.price for item in self.items), 0.0)


class Customer:
    """A customer and their past purchase history."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.purchase_history: list[Order] = []

    def add_order(self, order: Order) -> None:
        self.purchase_history.append(order)


if __name__ == "__main__":
    burger = FoodItem("Spicy Burger", 8.99, "Food", 4.5)
    soda = FoodItem("Large Soda", 2.49, "Drinks", 4.0)
    cookie = FoodItem("Cookie", 1.99, "Desserts", 4.8)

    menu = Menu()
    for item in (burger, soda, cookie):
        menu.add_item(item)
    assert menu.filter_by_category("drinks") == [soda]
    assert menu.filter_by_category("Salads") == []

    assert Order().compute_total() == 0.0
    order = Order()
    order.add_item(burger)
    order.add_item(soda)
    order.add_item(soda)
    assert abs(order.compute_total() - (8.99 + 2.49 * 2)) < 1e-9

    customer = Customer("Alice")
    customer.add_order(order)
    assert len(customer.purchase_history) == 1

    print("All checks passed.")
