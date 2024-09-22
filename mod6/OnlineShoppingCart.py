# Lincoln Quick
# CSC 500, Module 6, Portfolio Milestone
# 2024-09-01
# Modified 2024-09-22
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
from ShoppingCart import ShoppingCart
import datetime

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
            print("\nADD ITEM TO CART")
            itemToAdd = build_item()
            cart.add_item(itemToAdd)
        elif choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            itemNameToRemove = prompt_user_for_item_name()
            cart.remove_item(itemNameToRemove)
        elif choice == 'c':
            # Prompt the user for the item name and quantity
            print("\nCHANGE ITEM QUANTITY")
            # TODO
        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
        else:
            print("\nInvalid choice. Please try again.")
        choice = input("Choose an option: ")

# Main function
def main():
    # Create a shopping cart
    customer_name = input("Enter your name: ")
    # Get the current date, formatted to Month Day, Year
    date = datetime.date.today().strftime("%B %d, %Y")

    cart = ShoppingCart(customer_name, date)
    print_menu(cart)

# Define build_item() function
def build_item():
    
    item_name = input('Enter the item name: ')
    item_price = float(input('Enter the item price: '))
    item_quantity = int(input('Enter the item quantity: '))
    item_description = input('Enter the item description: ')
    item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
    return item

# Define prompt_user_for_item_name() function
def prompt_user_for_item_name():
    item_name = input('Enter the item name: ')
    return item_name

if __name__ == "__main__":
    main()