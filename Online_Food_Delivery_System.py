class User:

    def __init__(self,name,phone_number,address):
        self.name = name
        self.phone_number = phone_number
        self.address = address

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise ValueError("Name must be in string")
        
        if value.strip() == "":
            raise ValueError("Name must not be empty")
        
        self.__name = value

    @property
    def phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self,number):
        if not isinstance(number,int):
            raise ValueError("Phone Number must be numeric")
        
        if len(str(number)) != 10:
            raise ValueError("Phone Number must be exactly 10 digit")
        
        self.__phone_number = number

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self,value):

        if not isinstance(value,str):
            raise ValueError("Address must be String")
        
        if value.strip() == "":
            raise ValueError("Address must not be empty")
        
        self.__address = value

    def display_info(self):
        return str(self)
    
    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Phone Number: {self.phone_number}\n"
            f"Address: {self.address}"
        )
    
class Customer(User):

    customer_id = 1

    def __init__(self,name,phone_number,address,wallet_balance):
        super().__init__(name,phone_number,address)
        self.customer_id = f"C{Customer.customer_id:03}"
        Customer.customer_id += 1
        self.wallet_balance = wallet_balance
        self.orders = []

    @property
    def wallet_balance(self):
        return self.__wallet_balance
    
    @wallet_balance.setter
    def wallet_balance(self,amount):
        if not isinstance(amount,(int,float)):
            raise ValueError("Amount must be numeric")
        
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        
        self.__wallet_balance = amount

    def add_money(self,amount):
        if not isinstance(amount,(int,float)):
            raise ValueError("Amount must be numeric")
        
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        
        self.wallet_balance += amount
        return self.wallet_balance
    
    def add_order(self,order):
        self.orders.append(order)

    def display_info(self):
        return str(self)
    
    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Customer ID: {self.customer_id}\n"
            f"Wallet Balance: {self.wallet_balance}\n"
            f"Orders: {self.orders}"
        )
    
class DeliveryBoy(User):

    delivery_counter = 1

    def __init__(self,name,phone_number,address,salary):
        super().__init__(name,phone_number,address)
        self.delivery_boy_id = f"D{DeliveryBoy.delivery_counter:03}"
        DeliveryBoy.delivery_counter += 1
        self.salary = salary
        self.available = True

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,amount):
        if not isinstance(amount,(int,float)):
            raise ValueError("Amount should be numeric")
        
        if amount <= 0:
            raise ValueError("Amount should be greater then 0")
        
        self.__salary = amount
        
    def change_status(self,value):
        if not isinstance(value,bool):
            raise ValueError("Status must be a Boolean value")
        
        self.available = value
        return self.available

    def display_info(self):
        return str(self)
    
    def increase_salary(self,amount):
        if not isinstance(amount,(int,float)):
            raise ValueError("Amount should be numeric")
        
        if amount <= 0:
            raise ValueError("Amount should be greater then 0")
        
        self.salary += amount
        return self.salary

    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Delivery_ID: {self.delivery_boy_id}\n"
            f"Salary: {self.salary}\n"
            f"Status: {self.available}"
        )
    
class FoodItem:

    def __init__(self,food_item,price,category):
        self.food_item = food_item
        self.price = price
        self.category = category

    @property
    def food_item(self):
        return self.__food_item
    
    @food_item.setter
    def food_item(self,value):
        if not isinstance(value,str):
            raise ValueError("Food Item must be string")
        
        if value.strip() == "":
            raise ValueError("Food Item must not be empty")
        
        self.__food_item = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,amount):
        if not isinstance(amount,(int,float)):
            raise ValueError("Price must be numerical")
        
        if amount <= 0:
            raise ValueError("Price must be greater then 0")
        
        self.__price = amount

    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self,value):
        if not isinstance(value,str):
            raise ValueError("Category must be in string")
        
        if value.strip() == "":
            raise ValueError("Category must not be empty")
        
        self.__category = value

    def __str__(self):
        return (
            f"Food: {self.food_item}, "
            f"Price: ₹{self.price}, "
            f"Category: {self.category}"
        )
    
class Resturant:

    resturant_id = 1

    def __init__(self,resturant_name,rating):
        self.resturant_name = resturant_name
        self.resturant_id = f"R{Resturant.resturant_id:03}"
        Resturant.resturant_id += 1
        self.rating = rating
        self.menu = []

    @property
    def resturant_name(self):
        return self.__resturant_name
    
    @resturant_name.setter
    def resturant_name(self,value):
        if not isinstance(value,str):
            raise ValueError("Resturant Name must be string")
        
        if value.strip() == "":
            raise ValueError("Resturant Name must not be empty")
        
        self.__resturant_name = value

    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError("Rating must be numerical")
        
        if value < 0 or value > 10:
            raise ValueError("Give rating correctly")
        
        self.__rating = value

    def add_food(self,food):
        if not isinstance(food,FoodItem):
            raise ValueError("Food must be string")
        
        for item in self.menu:
            if item.food_item == food.food_item:
                raise ValueError("Food is already in menu")
            
        self.menu.append(food)
        print(f"{food} Added succesfully to the menu")

    def remove_food(self,food):
        for item in self.menu:
            if item.food_item == food:
                self.menu.remove(item)
                print(f"{food} Successfully removed from the menu")
                return
            
        raise ValueError("Food not found") 

    def show_menu(self):
        for food in self.menu:
            print(food)

class Order:

    order_id = 1

    def __init__(self,customer,resturant,foods):
        self.order_id = f"O{Order.order_id:03}"
        Order.order_id += 1
        self.customer = customer
        self.resturant = resturant
        self.delivery_boy = None
        self.foods = foods
        self.status = "Preparing"

    @property
    def customer(self):
        return self.__customer
    
    @customer.setter
    def customer(self,value):
        if not isinstance(value,Customer):
            raise ValueError("Customer must contain customer object")
        
        self.__customer = value

    @property
    def resturant(self):
        return self.__resturant
    
    @resturant.setter
    def resturant(self,value):
        if not isinstance(value,Resturant):
            raise ValueError("Resturant must contain Resturant object")
        
        self.__resturant = value

    @property
    def delivery_boy(self):
        return self.__delivery_boy
    
    @delivery_boy.setter
    def delivery_boy(self,value):
        if value is not None and not isinstance(value,DeliveryBoy):
            raise ValueError("Delivery Boy must contain DeliveryBoy object")
        
        self.__delivery_boy = value

    @property
    def foods(self):
        return self.__food
    
    @foods.setter
    def foods(self,value):
        if not isinstance(value,list):
            raise ValueError("Foods must be a list")
        
        if len(value) == 0:
            raise ValueError("Order must contain at least one food item")
        
        for food in value:
            if not isinstance(food,FoodItem):
                raise ValueError("Food must contains Food objects")
            
        self.__food = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        valid_status = (
            "Preparing",
            "Out for Delivery",
            "Delivered",
            "Cancelled"
        )

        if value not in valid_status:
            raise ValueError("Invalid order status")

        self.__status = value

    def change_status(self,status):
        self.status = status

    def calculate_bill(self):
        total = 0

        for food in self.foods:
            total += food.price

        return total
    
    def __str__(self):
        return (
            f"Order ID: {self.order_id}\n"
            f"Customer: {self.customer.name}\n"
            f"Restaurant: {self.resturant.resturant_name}\n"
            f"Delivery Boy: {self.delivery_boy.name}\n"
            f"Status: {self.status}\n"
            f"Total Bill: ₹{self.calculate_bill()}"
        )
    
    def __repr__(self):
        return self.__str__()
    
class FoodDeliverySystem:

    def __init__(self):
        self.customers = []
        self.resturants = []
        self.delivery_boys = []
        self.orders = []

    def add_customer(self,value):
        if not isinstance(value,Customer):
            raise ValueError("Customer must contain customer object")
        
        self.customers.append(value)

    def remove_customer(self,customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                self.customers.remove(customer)
                return
            
        raise ValueError("Customer not found")
    
    def search_customer(self,customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
            
        raise ValueError("Customer Not found")
    
    def add_resturant(self,value):
        if not isinstance(value,Resturant):
            raise ValueError("Customer must contain customer object")
        
        self.resturants.append(value)

    def remove_resturant(self,rest_id):
        for rest in self.resturants:
            if rest.resturant_id == rest_id:
                self.resturants.remove(rest)
                return
            
        raise ValueError("Resturant that you want to remove doesn't found")
    
    def search_restaurant(self,rest_id):
        for rest in self.resturants:
            if rest.resturant_id == rest_id:
                return rest
            
        raise ValueError("Resturant not found")
    
    def add_delivery_boy(self,name):
        if not isinstance(name,DeliveryBoy):
            raise ValueError("Delivery boy must contain delivery boy object")
        
        self.delivery_boys.append(name)

    def change_delivery_status(self,id,status):
        for boy in self.delivery_boys:
            if boy.delivery_boy_id == id:
                boy.change_status(status)
                return
            
        raise ValueError("Delivery boy not found")
    
    def increase_salary(self,id,amount):
        for boy in self.delivery_boys:
            if boy.delivery_boy_id == id:
                boy.increase_salary(amount)
                return
        
        raise ValueError("Delivery boy not found")
    
    def add_food(self,rest_id ,food):
        resturant = self.search_restaurant(rest_id)
        resturant.add_food(food)

    def remove_food(self,rest_id,food):
        resturants = self.search_restaurant(rest_id)
        resturants.remove_food(food)

    def place_order(self, order):

        if not isinstance(order, Order):
            raise ValueError("Order must contain an Order object.")

        for existing_order in self.orders:
            if existing_order.order_id == order.order_id:
                raise ValueError("Order already exists.")
            
        total_bill = order.calculate_bill()

        if order.customer.wallet_balance < total_bill:
            raise ValueError("Insufficient wallet balance.")

        available_boy = None

        for boy in self.delivery_boys:
            if boy.available:
                available_boy = boy
                break

        if available_boy is None:
            raise ValueError("No delivery boy is available.")

        order.delivery_boy = available_boy

        available_boy.change_status(False)

        order.customer.wallet_balance -= total_bill

        self.orders.append(order)

        order.customer.add_order(order)

        print(
            f"Order {order.order_id} placed successfully.\n"
            f"Total Bill: ₹{total_bill}"
        )

    def cancel_order(self,ord_id):
        for order in self.orders:
            if order.order_id == ord_id:
                self.orders.remove(order)
                return

        raise ValueError("Order doesn't found")
    
    def deliver_order(self,order_id):

        for order in self.orders:

            if order.order_id == order_id:

                if order.status == "Cancelled":
                    raise ValueError("Cancelled order cannot be delivered.")

                if order.status == "Delivered":
                    raise ValueError("Order has already been delivered.")

                if order.status != "Out for Delivery":
                    raise ValueError("Order is not out for delivery.")
            
                order.change_status("Delivered")
                order.delivery_boy.change_status(True)

                print("Order delivered succesfully")
                return
            
        raise ValueError("Order not found")
    
    def show_orders(self):
        return self.orders

system = FoodDeliverySystem()

c1 = Customer("Mayur", 9876543210, "Mumbai", 1000)

d1 = DeliveryBoy("Rahul", 9876543211, "Thane", 25000)
d2 = DeliveryBoy("Amit", 9876543212, "Navi Mumbai", 22000)

r1 = Resturant("Pizza Hub", 4.8)

f1 = FoodItem("Pizza", 300, "Fast Food")
f2 = FoodItem("Burger", 150, "Fast Food")
f3 = FoodItem("Fries", 120, "Snacks")

system.add_customer(c1)

system.add_delivery_boy(d1)
system.add_delivery_boy(d2)

system.add_resturant(r1)

system.add_food(r1.resturant_id, f1)
system.add_food(r1.resturant_id, f2)
system.add_food(r1.resturant_id, f3)

order1 = Order(
    c1,
    r1,
    [f1, f2]
)

system.place_order(order1)

print(order1.calculate_bill())

print(c1.wallet_balance)

print(d1.available)

print(c1.orders)

'''
c2 = Customer(
    "Rohan",
    9999999999,
    "Pune",
    100
)

order2 = Order(
    c2,
    r1,
    [f1, f2]
)

system.place_order(order2)


d1.change_status(False)
d2.change_status(False)

order3 = Order(
    c1,
    r1,
    [f3]
)

system.place_order(order3)

system.add_food(r1.resturant_id, f1)
'''

system.remove_food(
    r1.resturant_id,
    "Burger"
)

print(
    system.search_customer(
        c1.customer_id
    )
)

# system.cancel_order("O999")