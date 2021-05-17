"""This module describes cafe work system.

Exercise: Create program that describes Cafe with
food delivery. It should consists of 10 classes and follows
OOP principles (Inheritance and Encapsulation). Access
modifiers and static methods are required.
"""


class Owner:
    """Creates Owner class, it`s private info and money_balance"""
    _address = ''
    _contact_number = None
    email = ''
    cafes = {}
    money_balance = 3000

    def __init__(self, name):
        self.name = name

    def get_profit(self, money_count, cafe_name: object):
        """This method gets transfers money from the cafe account to the owner's account"""
        self.money_balance += money_count
        cafe_name.money_balance -= money_count

    def add_new_cafe(self, new_cafe_name: str, new_cafe_adress: str, new_cafe_capacity: int):
        """Method allows Owner to create and add new cafe to the dict {cafe}"""
        self.cafes[new_cafe_name] = [new_cafe_adress, new_cafe_capacity]


class Cafe:
    """Creates class Cafe with main info, menu list, employee list and money_balance"""
    contact_number = None
    opening_hours = "8.00 - 23.00"
    email = ''
    web_site = ''
    is_open = True
    menu_list = ['starters', 'mains', 'desserts', 'cocktails']
    employees = {}
    money_balance = 1500

    def __init__(self, name: str, address: str, capacity: int):
        self.name = name
        self.address = address
        self.capacity = capacity

    def add_employee(self, name, position):
        """Method adds employee to the 'employee' dict"""
        self.employees[name] = position

    def remove_employee(self, name):
        """Method removes employee from the dict {employee}'"""
        del self.employees[name]

    def add_menu_section(self, section_name):
        """Method adds menu section to the list [menu_list]"""
        self.menu_list.append(section_name)

    def remove_menu_section(self, section_name: str):
        """Method removes menu section from the list [menu_list]"""
        self.menu_list.remove(section_name)


class Table:
    """Creates class Table with table ID and capacity"""
    all_tables = {}

    def __init__(self, table_id, capacity):
        self.capacity = capacity
        self.table_id = table_id
        self.all_tables[table_id] = capacity

    def show_all_tables(self):
        """Method shows all tables with capacity"""
        for table in self.all_tables:
            print(f"Table №{table}: for {self.all_tables[table][0]} pers.")

    def remove_table(self, table_id):
        """Method removes table from dict {all_table}"""
        del self.all_tables[table_id]


class MenuSection:
    """Creates class MenuSection with main info and item list"""
    _id = 0
    description = ''
    item_list = []

    def __init__(self, title: str):
        self.title = title
        MenuSection._id += 1

    def add_item(self, item: str):
        """Method adds item to the list [item_list]"""
        self.item_list.append(item)

    def remove_item(self, item: str):
        """Method removes menu section from the list [item_list]"""
        self.item_list.remove(item)

    def get_all_items(self):
        """Method shows all items from the list [item_list] in current menu section"""
        print(f"List of Menu Section '{self.title}': {self.item_list}")


class Item:
    """Creates class MenuSection with name, price and description"""
    price = 0
    name = None
    _id = 0
    description = ''

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        Item._id += 1

    def set_price(self, new_price: int):
        """Method sets new price for item"""
        self.price = new_price

    def set_description(self, description: str):
        """Method sets description of current item"""
        self.description = description


class Order:
    """Creates class MenuSection with name, price and description"""
    id = 0
    item_list = {}
    total_price = 0
    delivery_address = ''

    def __init__(self):
        Order.id += 1
        self.status = None

    def set_status(self, new_status: str):
        """Method sets order status"""
        self.status = new_status

    def add_item(self, item_name: object, quantity: int, price: int):
        """Method adds item to the orders`s list [item_list]"""
        self.item_list[item_name] = [quantity, price]

    def remove_item(self, item_name):
        """Method removes item from the orders`s list [item_list]"""
        del self.item_list[item_name]

    def show_order(self):
        """Method shows all items in current order"""
        for item in self.item_list:
            print(f"{item}: ${self.item_list[item][1]} {self.item_list[item][0]} pc.")

    def show_total_price(self):
        """Method shows total price of the current order"""
        for item in self.item_list:
            self.total_price += self.item_list[item][0] * self.item_list[item][1]
        print(self.total_price)


class DeliveryInfo:
    """Creates class DeliveryInfo with main info"""
    contact_number = None
    status = None

    def __init__(self, order_obj: object, address):
        self.order_id = order_obj.id
        self.address = address

    def set_contact_number(self, customer_obj):
        """Method sets contact number of customer given in attribute"""
        self.contact_number = customer_obj.comtact_number

    def set_status(self, new_status: str):
        """Method sets new delivery status to the current order"""
        self.status = new_status


class Customer:
    """Creates class Customer with main info"""
    _id = 0
    _contact_number = ''
    __username = ''
    __password = ''
    _address = ''
    delivery = False

    def __init__(self, name, cash_balance):
        Customer._id += 1
        self.name = name
        self.cash_balance = cash_balance

    def pay_order(self, order_name: object, order_total_price: object):
        """Method allows customer to pay order and show order`s ID and it˜s total price"""
        self.cash_balance -= order_total_price
        print(f"Ypu`ve just paid order №{order_name}, total price: {order_total_price}. Thank you!")

    def delivery_order(self):
        """Method switches delivery status to 'True'"""
        self.delivery = True


class Employee:
    """Creates class Employee with main info and order list"""
    _id = 0
    _contact_number = ''
    __username = ''
    __password = ''
    position = ''
    salary = 0
    orders_list = {}
    order_activity = {}

    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def add_new_order(self, order_id: object, order_item_list: object):
        """Method adds ID and item list of new order to the [order_list]"""
        self.orders_list[order_id] = order_item_list

    def order_status(self, order_id: object, new_status: str):
        """Method adds ID and status of new order to the [order_activity]"""
        self.order_activity[order_id] = new_status


class Waiter(Employee):
    """Creates class Waiter that inherits from class Employee"""
    serving_tables = {}

    def __init__(self, name, salary, position="Waiter"):
        super().__init__(name, salary, position)

    def start_serve_table(self, table_number: object, order_id: object):
        """Method allow Waiter to start serving table
        and adds table's ID and order`s ID to the dict {cafe_tables}"""
        self.serving_tables[table_number.id] = order_id.id

    def show_serving_tables(self):
        """Method shows all tables serving by Waiter"""
        for table in self.serving_tables:
            print(f"Table №{table} has order №{self.serving_tables[table]}")


class Cook(Employee):
    """Creates class Cook that inherits from class Employee"""
    def __init__(self, name, salary, position="Cook"):
        super().__init__(name, salary, position)

    def prepare_item(self, item_name: object, quantity: object, order_id: object):
        """Method allows to Cook to prepare item and shows the process
        with item`s name, quantity and order`s id"""
        print(f"Cook {self.name} has cooked {item_name}"
              f"in quantity {quantity} for order №{order_id}")


class Administrator(Employee):
    """Creates class Administrator that inherits from class Employee
    with new static attribute - employee_bonuses"""
    employee_bonuses = {}

    def __init__(self, name, salary, position="Administrator"):
        super().__init__(name, salary, position)

    def cancel_order(self, order_id):
        """Method allows Administrator to cancel the order"""
        del self.order_activity[order_id]
        del self.orders_list[order_id]

    def set_employee_bonus(self, employee_name: object,
                           employee_position: object,
                           bonus_amount: int):
        """Method allows Administrator to set bonus for employee"""
        self.employee_bonuses[employee_name] = [employee_position, bonus_amount]

    @staticmethod
    def set_cash_balance(cafe_obj: object, new_balance: int):
        """Method allows Administrator to set money balance of the cafe"""
        cafe_obj.money_balance += new_balance


gorcafe = Cafe('ZuZu', 'Kharkiv, Ukraine', 120)
nikita = Owner('Nikita Feoktistov')
gorcafe.add_employee('Vasiliy', 'waiter')
table1 = Table(1, 4)
customer_1 = Customer('david', 1000)
admin1 = Administrator('Olya', 2000)
waiter1 = Waiter('Vasiliy', 500)
order_1 = Order()
item_1 = Item('meat', 100)
item_2 = Item('coffee', 15)

print(gorcafe.name)
print(gorcafe.employees)
print(gorcafe.money_balance, nikita.money_balance)
nikita.get_profit(500, gorcafe)
print(gorcafe.money_balance, nikita.money_balance)

order_1.add_item(item_1.name, 1, 150)
order_1.add_item(item_2.name, 2, 25)
print(order_1.item_list)

order_1.show_order()
order_1.show_total_price()

customer_1.pay_order(order_1.id, order_1.total_price)
print(customer_1.cash_balance)

admin1.set_cash_balance(gorcafe, 654)
print(gorcafe.money_balance)

waiter1.start_serve_table(table1, order_1)
waiter1.show_serving_tables()
