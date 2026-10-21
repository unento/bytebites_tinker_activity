# ByteBites — UML Class Diagram

```mermaid
classDiagram
    class Customer {
        +str name
        +list~Order~ purchase_history
        +add_order(order: Order) None
        +is_verified() bool
    }

    class FoodItem {
        +str name
        +float price
        +str category
        +float popularity_rating
    }

    class Menu {
        +list~FoodItem~ items
        +add_item(item: FoodItem) None
        +filter_by_category(category: str) list~FoodItem~
        +sort_by_popularity() list~FoodItem~
    }

    class Order {
        +list~FoodItem~ items
        +add_item(item: FoodItem) None
        +compute_total() float
    }

    Customer "1" --> "0..*" Order : places
    Menu "1" o-- "0..*" FoodItem : contains
    Order "0..*" o-- "1..*" FoodItem : includes
```

## Design notes

- **Customer.is_verified()** returns `True` if the customer has at least one past order.
- **Menu.filter_by_category()** matches categories case-insensitively ("drinks" matches "Drinks") and returns an empty list if nothing matches.
- **Menu.sort_by_popularity()** returns items sorted by `popularity_rating`, highest first. This is the simple "smart" hook for recommendations.
- **Order.compute_total()** sums the item prices. An empty order totals `0.0`.
- **Quantities**: ordering two of the same item means adding it twice. There is no separate quantity field.
- **Order → Customer**: an order does not store its customer. The link goes only from `Customer` to its orders through `purchase_history`, which avoids a circular reference.
- **Aggregation (◇)**: `FoodItem`s exist on their own. Menus and orders reference them but don't own them.
