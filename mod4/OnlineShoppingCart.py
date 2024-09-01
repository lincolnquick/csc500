# Lincoln Quick
# CSC 500, Module 4, Portfolio Milestone
# 2024-09-01

from ItemToPurchase import ItemToPurchase

# create a list to hold all items in the shopping cart
items = []

def prompt_user_for_item():
    item = ItemToPurchase()
    item.set_item_name(input('Enter the item name:\n'))
    item.set_item_price(float(input('Enter the item price:\n')))
    item.set_item_quantity(int(input('Enter the item quantity:\n')))
    return item

def show_items_and_total_cost(items):
    total_cost = 0
    for item in items:
        item.print_item_cost()
        total_cost += item.get_item_price() * item.get_item_quantity()
    print('Total: ${0}'.format(total_cost))