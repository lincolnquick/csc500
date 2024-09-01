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

    