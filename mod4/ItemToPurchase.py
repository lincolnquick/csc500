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

    
    