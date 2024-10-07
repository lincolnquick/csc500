# Lincoln Quick
# CSC 500: Module 6 Portfolio Milestone
# 2024-09-01
# Modified 2024-10-06

# "Online Shopping Cart
# Step 4: Build the ShoppingCart class with the following data attributes and related methods. 
# Note: Some can be method stubs (empty methods) initially, to be completed in later steps

# Parameterized constructor, which takes the customer name and date as parameters
#Attributes
#customer_name (string) - Initialized in default constructor to "none"
#current_date (string) - Initialized in default constructor to "January 1, 2020"
#cart_items (list)
#Methods
#add_item()
#Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
#remove_item()
#Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
#If item name cannot be found, output this message: Item not found in cart. Nothing removed.
#modify_item()
#Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
#If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
#If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
#get_num_items_in_cart()
#Returns quantity of all items in cart. Has no parameters.
#get_cost_of_cart()
#Determines and returns the total cost of items in cart. Has no parameters.
#print_total()
#Outputs total of objects in cart.
#If cart is empty, output this message: SHOPPING CART IS EMPTY
#print_descriptions()
#Outputs each item's description.
#Example of print_total() output:
#John Doe's Shopping Cart - February 1, 2020
#Number of Items: 8
#Nike Romaleos 2 @ $189 = $378
#Chocolate Chips 5 @ $3 = $15
#Powerbeats 2 Headphones 1 @ $128 = $128
#Total: $521

#Example of print_descriptions() output:
#John Doe's Shopping Cart - February 1, 2020
#Item Descriptions
#Nike Romaleos: Volt color, Weightlifting shoes
#Chocolate Chips: Semi-sweet
#Powerbeats 2 Headphones: Bluetooth headphones

# Import ItemToPurchase class
from ItemToPurchase import ItemToPurchase

class ShoppingCart:
    # Default Constructor
    def __init__(self):
        self.customer_name = 'none'
        self.current_date = 'January 1, 2020'
        self.cart_items = []

    # Parameterized Constructor
    def __init__(self, customer_name, current_date):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Getters and Setters
    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def get_customer_name(self):
        return self.customer_name
    
    def set_current_date(self, current_date):
        self.current_date = current_date

    def get_current_date(self):
        return self.current_date
    
    
    # Method to add an item to the cart
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        print("Item added to cart.")

    # Method to remove an item from the cart
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.get_item_name() == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    # Method to modify an item in the cart
    def modify_item(self, ItemToPurchase):
        for item in self.cart_items:
            if item.get_item_name() == ItemToPurchase.get_item_name():
                if ItemToPurchase.get_item_price() != 0:
                    item.set_item_price(ItemToPurchase.get_item_price())
                if ItemToPurchase.get_item_quantity() != 0:
                    item.set_item_quantity(ItemToPurchase.get_item_quantity())
                return
        print("Item not found in cart. Nothing modified.")

    # Method to get the number of items in the cart
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.get_item_quantity()
        return num_items
    
    # Method to get the total cost of the items in the cart
    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.get_item_price() * item.get_item_quantity()
        return total_cost
    
    # Method to print the descriptions of the items in the cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.get_item_name()}: {item.get_item_description()}")
    
    # Method to print the total cost of the items in the cart
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
            return
        for item in self.cart_items:
            item.print_item_cost()
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost}")





    
