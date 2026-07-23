# 🍔 Online Food Delivery System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Paradigm-OOP-FF6F00?style=for-the-badge" alt="OOP">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
  <img src="https://img.shields.io/github/stars/Mayurchotaliya07/Online_Food_Delivery_System?style=for-the-badge" alt="GitHub Stars">
  <img src="https://img.shields.io/github/forks/Mayurchotaliya07/Online_Food_Delivery_System?style=for-the-badge" alt="GitHub Forks">
  <img src="https://img.shields.io/github/last-commit/Mayurchotaliya07/Online_Food_Delivery_System?style=for-the-badge" alt="Last Commit">
</p>

<p align="center">
  A fully object-oriented, console-based simulation of a real-world food delivery platform — built entirely in core Python.
</p>

---

## 📖 1. Project Overview

The **Online Food Delivery System** is a console-based application that simulates the core operations of a real-world food delivery platform (think Swiggy/Zomato-style workflows) entirely through **Object-Oriented Programming (OOP) in Python**.

It models the complete lifecycle of a food order — from registering customers and restaurants, building a food menu, placing an order, assigning a delivery partner, calculating the bill, deducting the customer's wallet balance, and finally marking the order as delivered.

### Problem It Solves

Food delivery platforms need to coordinate several independent entities — customers, restaurants, menus, delivery agents, orders, and payments — while enforcing strict business rules (no negative wallet balances, no duplicate menu items, no double-booking a delivery boy, etc.). This project demonstrates how such a system can be modeled cleanly using classes, encapsulation, inheritance, and validation logic, without relying on any external framework or database.

It serves as a strong **portfolio project** to demonstrate real-world application of Python OOP fundamentals — not just syntax, but system design thinking.

---

## ✨ 2. Features

- 👤 **Customer Management** — register, search, and remove customers
- 🏬 **Restaurant Management** — register, search, and remove restaurants
- 🍕 **Food Menu Management** — add/remove food items per restaurant
- 🛵 **Delivery Boy Management** — register delivery partners, track availability
- 📦 **Order Placement** — place multi-item orders tied to a customer & restaurant
- 💰 **Wallet System** — add funds, auto-deduct on order placement
- 🧾 **Automatic Bill Calculation** — computed from live food prices
- 📋 **Dynamic Food Menu** — restaurants maintain their own menu list
- 🚴 **Automatic Delivery Assignment** — assigns the first available delivery boy
- 🔄 **Order Status Tracking** — `Preparing → Out for Delivery → Delivered / Cancelled`
- ❌ **Order Cancellation** — remove pending orders
- ✅ **Input Validation** — every attribute is validated before assignment
- 🚨 **Exception Handling** — descriptive `ValueError` raised for every invalid operation
- 🔒 **Encapsulation** — private attributes (`__name` style) accessed only via properties
- 🧬 **Inheritance** — `Customer` and `DeliveryBoy` both inherit from `User`
- ⚙️ **Properties (Getters/Setters)** — used throughout for controlled attribute access
- 💵 **Salary Management** — increase delivery boy salary with validation
- 🆔 **Auto-Generated IDs** — `C001`, `D001`, `R001`, `O001` style unique IDs via class counters

---

## 🛠️ 3. Technologies Used

| Technology              | Purpose                                   |
| ------------------------ | ------------------------------------------ |
| **Python 3**             | Core backend logic                         |
| **OOP (Classes/Objects)**| Project architecture & design              |
| **Property Decorators**  | Encapsulation & controlled data access     |
| **Exception Handling**   | Business rule enforcement (`ValueError`)   |
| **VS Code**              | Development environment                    |
| **Git & GitHub**         | Version control & hosting                  |

---

## 📁 4. Project Structure

```
Online_Food_Delivery_System/
│
├── Online_Food_Delivery_System.py     # Complete OOP source code
└── README.md                          # Project documentation
```

---

## 🧩 5. Class Diagram & Explanation

<details>
<summary><strong>👤 User (Base Class)</strong></summary>

**Purpose:** Base class holding common personal details shared by every person in the system.

**Attributes:** `name`, `phone_number`, `address` (all private, exposed via properties)

**Methods:** `display_info()`, `__str__()`

**Relationship:** Parent class of `Customer` and `DeliveryBoy` (Inheritance)
</details>

<details>
<summary><strong>🙋 Customer(User)</strong></summary>

**Purpose:** Represents a customer who places orders.

**Attributes:** `customer_id` (auto-generated, e.g. `C001`), `wallet_balance`, `orders` (list)

**Methods:** `add_money()`, `add_order()`, `display_info()`, `__str__()`

**Relationship:** Inherits from `User`; referenced by `Order` (Composition); holds a list of `Order` objects
</details>

<details>
<summary><strong>🛵 DeliveryBoy(User)</strong></summary>

**Purpose:** Represents a delivery partner who fulfills orders.

**Attributes:** `delivery_boy_id` (auto-generated, e.g. `D001`), `salary`, `available` (boolean)

**Methods:** `change_status()`, `increase_salary()`, `display_info()`, `__str__()`

**Relationship:** Inherits from `User`; referenced by `Order` once assigned
</details>

<details>
<summary><strong>🍕 FoodItem</strong></summary>

**Purpose:** Represents a single dish sold by a restaurant.

**Attributes:** `food_item` (name), `price`, `category`

**Methods:** `__str__()`

**Relationship:** Stored in a `Resturant`'s `menu` list; referenced inside an `Order`'s `foods` list
</details>

<details>
<summary><strong>🏬 Resturant</strong></summary>

**Purpose:** Represents a restaurant that owns a menu of food items.

**Attributes:** `resturant_name`, `resturant_id` (auto-generated, e.g. `R001`), `rating`, `menu` (list of `FoodItem`)

**Methods:** `add_food()`, `remove_food()`, `show_menu()`

**Relationship:** Composed of multiple `FoodItem` objects; referenced by `Order`
</details>

<details>
<summary><strong>📦 Order</strong></summary>

**Purpose:** Represents a single food order, tying together a customer, restaurant, delivery boy, and food items.

**Attributes:** `order_id` (auto-generated, e.g. `O001`), `customer`, `resturant`, `delivery_boy`, `foods` (list), `status`

**Methods:** `change_status()`, `calculate_bill()`, `__str__()`, `__repr__()`

**Relationship:** References one `Customer`, one `Resturant`, one `DeliveryBoy`, and multiple `FoodItem` objects (Composition/Object References)
</details>

<details>
<summary><strong>🧠 FoodDeliverySystem (Controller Class)</strong></summary>

**Purpose:** The central orchestrator that manages every entity and business workflow in the system.

**Attributes:** `customers`, `resturants`, `delivery_boys`, `orders` (all lists)

**Methods:** `add_customer()`, `remove_customer()`, `search_customer()`, `add_resturant()`, `remove_resturant()`, `search_restaurant()`, `add_delivery_boy()`, `change_delivery_status()`, `increase_salary()`, `add_food()`, `remove_food()`, `place_order()`, `cancel_order()`, `deliver_order()`, `show_orders()`

**Relationship:** Aggregates and manages all other classes — the single entry point for all operations
</details>

---

## 🎓 6. OOP Concepts Used

| Concept                  | Where It's Used                                                              |
| ------------------------- | ------------------------------------------------------------------------------ |
| **Classes & Objects**     | Every entity (`Customer`, `Order`, `Resturant`, etc.) is a class instance     |
| **Encapsulation**         | All attributes stored as private (`self.__name`) and accessed via properties |
| **Inheritance**           | `Customer` and `DeliveryBoy` inherit shared logic from `User`                |
| **Properties**            | `@property` decorators used for every attribute across all classes           |
| **Getters & Setters**     | Every property has a paired getter and validating setter                     |
| **Composition**           | `Resturant` is composed of `FoodItem`s; `Order` is composed of a `Customer`, `Resturant`, `DeliveryBoy`, and `FoodItem`s |
| **Object References**     | `Order` stores direct references to `Customer`, `Resturant`, and `DeliveryBoy` objects rather than copies |
| **Method Overriding**     | `__str__()` and `display_info()` are overridden in `Customer` and `DeliveryBoy`, extending `User`'s base output via `super()` |
| **Validation Logic**      | Every setter validates type, emptiness, and business rules before assignment |
| **Class-Level Counters**  | `customer_id`, `delivery_boy_id`, `resturant_id`, and `order_id` use class attributes as auto-incrementing counters |

---

## 🔄 7. Workflow

```
Create Customer
      ↓
Create Restaurant
      ↓
Add Food Items to Menu
      ↓
Create Delivery Boys
      ↓
Create Order (Customer + Restaurant + Food Items)
      ↓
Place Order → System Auto-Assigns Available Delivery Boy
      ↓
Calculate Bill
      ↓
Deduct Wallet Balance
      ↓
Update Status → "Out for Delivery"
      ↓
Deliver Order → Status → "Delivered"
      ↓
Delivery Boy Marked Available Again
```

---

## ⚙️ 8. Installation

```bash
# Clone the repository
git clone https://github.com/Mayurchotaliya07/Online_Food_Delivery_System.git

# Navigate into the project directory
cd Online_Food_Delivery_System

# Run the application
python Online_Food_Delivery_System.py
```

> **Requirements:** Python 3.10 or higher (no external dependencies).

---

## 💻 9. Example Usage

```python
# 1. Create the system
system = FoodDeliverySystem()

# 2. Create a customer
c1 = Customer("Mayur", 9876543210, "Mumbai", 1000)
system.add_customer(c1)

# 3. Create a restaurant
r1 = Resturant("Pizza Hub", 4.8)
system.add_resturant(r1)

# 4. Add food items to the restaurant's menu
f1 = FoodItem("Pizza", 300, "Fast Food")
f2 = FoodItem("Burger", 150, "Fast Food")
system.add_food(r1.resturant_id, f1)
system.add_food(r1.resturant_id, f2)

# 5. Register delivery boys
d1 = DeliveryBoy("Rahul", 9876543211, "Thane", 25000)
system.add_delivery_boy(d1)

# 6. Create and place an order
order1 = Order(c1, r1, [f1, f2])
system.place_order(order1)

# 7. Deliver the order
order1.change_status("Out for Delivery")
system.deliver_order(order1.order_id)
```

---

## 🔎 10. Validations

| Validation                     | Rule Enforced                                              |
| ------------------------------- | -------------------------------------------------------------- |
| **Name / Address**              | Must be a non-empty string                                    |
| **Phone Number**                | Must be an integer with exactly 10 digits                     |
| **Wallet Balance**              | Must be numeric and greater than 0                             |
| **Salary**                      | Must be numeric and greater than 0                             |
| **Price (Food Item)**           | Must be numeric and greater than 0                             |
| **Category / Food Name**        | Must be a non-empty string                                     |
| **Rating (Restaurant)**         | Must be numeric, between 0 and 10                              |
| **Food Object Validation**      | Only `FoodItem` instances accepted in menus/orders             |
| **Restaurant Object Validation**| Only `Resturant` instances accepted by the system              |
| **DeliveryBoy Object Validation**| Only `DeliveryBoy` instances accepted by the system            |
| **Customer Object Validation**  | Only `Customer` instances accepted by the system                |
| **Order Object Validation**     | Only `Order` instances accepted for placement                   |
| **Order Foods List**            | Must be a non-empty list containing only `FoodItem` objects    |
| **Order Status**                | Must be one of `Preparing`, `Out for Delivery`, `Delivered`, `Cancelled` |
| **Delivery Status**             | Must be a boolean value                                        |

---

## 🚨 11. Exception Handling

The system raises descriptive `ValueError` exceptions for every invalid operation, including:

- Customer not found
- Restaurant not found
- Order not found
- Delivery boy not found
- Insufficient wallet balance
- No delivery boy available
- Duplicate food item in menu
- Food item not found (on removal)
- Order already exists
- Cancelled order cannot be delivered
- Order already delivered
- Order not yet out for delivery
- Invalid phone number format
- Invalid rating value
- Non-numeric or non-positive price/salary/wallet amount
- Empty or non-string name/address/food/category/restaurant name
- Invalid object type passed (e.g. passing a string instead of a `FoodItem`)

---

## 🖥️ 12. Sample Output

```
Food: Pizza, Price: ₹300, Category: Fast Food Added succesfully to the menu
Food: Burger, Price: ₹150, Category: Fast Food Added succesfully to the menu
Food: Fries, Price: ₹120, Category: Snacks Added succesfully to the menu

Order O001 placed successfully.
Total Bill: ₹450

450
550
False
[Order ID: O001
Customer: Mayur
Restaurant: Pizza Hub
Delivery Boy: Rahul
Status: Preparing
Total Bill: ₹450]

Burger Successfully removed from the menu

Name: Mayur
Phone Number: 9876543210
Address: Mumbai
Customer ID: C001
Wallet Balance: 550
Orders: [Order ID: O001 ...]
```

---

## 🚀 13. Future Improvements

- 💳 Payment Gateway Integration
- 🏷️ Discount Coupons & Offers
- ⭐ Ratings & Reviews for Delivery Experience
- 📜 Order History & Invoices
- 🔍 Restaurant Search & Filtering
- 📍 Location-Based Restaurant Support
- 🏙️ Multiple Restaurants per Locality
- ⏱️ Estimated Delivery Time
- 🛠️ Admin Panel
- 🗄️ Database Integration (SQLite/PostgreSQL)
- 🖼️ Graphical User Interface (Tkinter/PyQt)
- 🌐 Django REST API Backend
- 🔐 User Authentication & Login System
- 🔔 Real-Time Order Notifications

---

## 📚 14. Learning Outcomes

This project demonstrates practical, hands-on mastery of core Python OOP principles, including:

- Designing a multi-class system with clear **single-responsibility** boundaries
- Applying **inheritance** to avoid duplicated logic between related entities
- Using **encapsulation** and **property decorators** to enforce data integrity at the point of assignment
- Modeling **real-world relationships** between objects through composition and object references
- Implementing **defensive programming** through consistent validation and exception handling
- Designing a **controller class** (`FoodDeliverySystem`) that coordinates independent subsystems — a pattern used in real backend architectures

---

## 📸 15. Screenshots

<details>
<summary>Click to expand</summary>

> _Screenshots coming soon —
</details>

---

## 👨‍💻 16. Author

**Mayur Chotaliya**

- GitHub: [@Mayurchotaliya07](https://github.com/Mayurchotaliya07)

---

## 📄 17. License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

```
MIT License

Copyright (c) 2026 Mayur Chotaliya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

<p align="center">
  ⭐ If you found this project useful, consider giving it a star on GitHub!
</p>
