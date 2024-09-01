# Lincoln Quick
# CSC 500, Module 4, Portfolio Milestone
# 2024-09-01

from ItemToPurchase import ItemToPurchase

def prompt_user_for_item():
    item = ItemToPurchase()
    item.set_item_name(input('Enter the item name:\n'))
    item.set_item_price(float(input('Enter the item price:\n')))
    item.set_item_quantity(int(input('Enter the item quantity:\n')))
    return item