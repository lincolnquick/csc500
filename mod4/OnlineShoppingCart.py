# Lincoln Quick
# CSC 500, Module 4, Portfolio Milestone
# 2024-09-01

from ItemToPurchase import ItemToPurchase

# Create a list to hold all items in the shopping cart
items = []

# Prompt the user for items to add to the shopping cart
def prompt_user_for_item():
    item = ItemToPurchase()
    item.set_item_name(input('Enter the item name: '))
    item.set_item_price(float(input('Enter the item price: ')))
    item.set_item_quantity(int(input('Enter the item quantity: ')))
    return item

# Print each item in the shopping cart and the total cost of all items
def show_items_and_total_cost(items):
    # Begin with newline to separate the items from the prompt
    print()
    total_cost = 0
    for item in items:
        item.print_item_cost()
        total_cost += item.get_item_price() * item.get_item_quantity()
    print('Total: ${:.2f}'.format(total_cost))


# Prompt the user to add 2 items to the shopping cart
for i in range(2):
    items.append(prompt_user_for_item())

# Print each item in the shopping cart and the total cost of all items
show_items_and_total_cost(items)