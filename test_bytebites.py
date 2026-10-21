import pytest

from models import FoodItem, Menu, Order, Customer


@pytest.fixture
def burger():
    return FoodItem("Spicy Burger", 8.99, "Food", 4.5)


@pytest.fixture
def soda():
    return FoodItem("Large Soda", 2.49, "Drinks", 4.0)


@pytest.fixture
def cookie():
    return FoodItem("Cookie", 1.99, "Desserts", 4.8)


@pytest.fixture
def menu(burger, soda, cookie):
    m = Menu()
    m.add_item(burger)
    m.add_item(soda)
    m.add_item(cookie)
    return m


# FoodItem

def test_fooditem_stores_attributes(burger):
    assert burger.name == "Spicy Burger"
    assert burger.price == 8.99
    assert burger.category == "Food"
    assert burger.popularity_rating == 4.5


# Menu

def test_menu_starts_empty():
    assert Menu().items == []


def test_menu_add_item(burger):
    m = Menu()
    m.add_item(burger)
    assert m.items == [burger]


def test_filter_by_category_returns_matches(menu, soda):
    assert menu.filter_by_category("Drinks") == [soda]


def test_filter_by_category_is_case_insensitive(menu, soda):
    assert menu.filter_by_category("drinks") == [soda]
    assert menu.filter_by_category("DRINKS") == [soda]


def test_filter_by_category_no_match_returns_empty(menu):
    assert menu.filter_by_category("Salads") == []


# Order

def test_empty_order_total_is_zero():
    assert Order().compute_total() == 0.0


def test_order_add_item(burger):
    order = Order()
    order.add_item(burger)
    assert order.items == [burger]


def test_order_total_sums_prices(burger, soda):
    order = Order()
    order.add_item(burger)
    order.add_item(soda)
    assert order.compute_total() == pytest.approx(11.48)


def test_order_same_item_twice_counts_twice(soda):
    order = Order()
    order.add_item(soda)
    order.add_item(soda)
    assert order.compute_total() == pytest.approx(4.98)


# Customer

def test_new_customer_has_empty_history():
    customer = Customer("Alice")
    assert customer.name == "Alice"
    assert customer.purchase_history == []


def test_add_order_appends_to_history():
    customer = Customer("Alice")
    order = Order()
    customer.add_order(order)
    assert customer.purchase_history == [order]


def test_customer_multiple_orders():
    customer = Customer("Alice")
    first, second = Order(), Order()
    customer.add_order(first)
    customer.add_order(second)
    assert customer.purchase_history == [first, second]
