# Lincoln Quick
# CSC 500, Module 6, Portfolio Milestone
# 2024-09-22
#
#Step 5: In the main section of your code, implement the print_menu() function. 
# print_menu() has a ShoppingCart parameter and outputs a menu of options to manipulate the shopping cart. 
# Each option is represented by a single character. Build and output the menu within the function.

#If an invalid character is entered, continue to prompt for a valid choice. Hint: Implement Quit before implementing other options. Call print_menu() in the main() function. Continue to execute the menu until the user enters q to Quit.

#Example:
#MENU
#a - Add item to cart
#r - Remove item from cart
#c - Change item quantity
#i - Output items' descriptions
#o - Output shopping cart
#q - Quit
#Choose an option:

#Step 6: Implement Output shopping cart menu option. Implement Output item's description menu option.

#Example of shopping cart menu option:
#OUTPUT SHOPPING CART
#John Doe's Shopping Cart - February 1, 2020
#Number of Items: 8
#Nike Romaleos 2 @ $189 = $378
#Chocolate Chips 5 @ $3 = $15
#Powerbeats 2 Headphones 1 @ $128 = $128
#Total: $521

#Example of item description menu option.
#OUTPUT ITEMS' DESCRIPTIONS
#John Doe's Shopping Cart - February 1, 2020
#Item Descriptions
#Nike Romaleos: Volt color, Weightlifting shoes
#Chocolate Chips: Semi-sweet
#Powerbeats 2 Headphones: Bluetooth headphones

from ItemToPurchase import ItemToPurchase
from OnlineShoppingCart import OnlineShoppingCart

# Print the menu
def print_menu(cart):
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    choice = input("Choose an option: ")
    while choice != 'q':
        if choice == 'a':
            itemToAdd = build_item()
            cart.add_item(itemToAdd)
        elif choice == 'r':
            itemNameToRemove = prompt_user_for_item_name()
            cart.remove_item(itemNameToRemove)
        elif choice == 'c':
            cart.change_item_quantity()
        elif choice == 'i':
            cart.output_items_descriptions()
        elif choice == 'o':
            cart.output_shopping_cart()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")
        choice = input("Choose an option: ")

# Main function
def main():
    # Create a shopping cart
    cart = OnlineShoppingCart()
    print_menu(cart)

# Define build_item() function
def build_item():
    item = ItemToPurchase()
    item.set_item_name(input('Enter the item name: '))
    item.set_item_price(float(input('Enter the item price: ')))
    item.set_item_quantity(int(input('Enter the item quantity: ')))
    item.set_item_description(input('Enter the item description: '))
    return item

# Define prompt_user_for_item_name() function
def prompt_user_for_item_name():
    item_name = input('Enter the item name: ')
    return item_name