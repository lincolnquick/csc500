# Lincoln Quick
# CSC 500, Module 4, Portfolio Milestone
# 2024-09-01

# "Online Shopping Cart

# Step 1: Build the ItemToPurchase class with the following specifications:

# Attributes
# item_name (string)
# item_price (float)
# item_quantity (int)
# Default constructor
# Initializes item's name = "none", item's price = 0, item's quantity = 0
# Method
# print_item_cost()
# Example of print_item_cost() output:
# Bottled Water 10 @ $1 = $10"

class ItemToPurchase:

    # Default constructor
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0

    # Method to print the item cost
    def print_item_cost(self):
        print('{0} {1} @ ${2} = ${3}'.format(self.item_name, self.item_quantity, self.item_price, self.item_price * self.item_quantity))

    # Getters and setters
    def set_item_name(self, item_name):
        self.item_name = item_name
    
    def get_item_name(self):
        return self.item_name
    
    def set_item_price(self, item_price):
        self.item_price = item_price

    def get_item_price(self):
        return self.item_price
    
    def set_item_quantity(self, item_quantity):
        self.item_quantity = item_quantity

    def get_item_quantity(self):
        return self.item_quantity
    