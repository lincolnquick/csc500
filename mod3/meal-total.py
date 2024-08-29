# Lincoln Quick
# CSC 500, Module 3, Critical Thinking Assignment Part 1
# 2024-08-29

# "Write a program that calculates the total amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the charge for the food and then calculate the 
# amounts with an 18 percent tip and 7 percent sales tax. 
# Display each of these amounts and the total price."

# Get the input for the meal subtotal from the user
meal_subtotal = float(input('Enter the charge for the food: '))

# Calculate the tip amount (18% of the meal subtotal)
tip_percent = 0.18
tip_amount = meal_subtotal * tip_percent

# Calculate the sales tax amount (7% of the meal subtotal)
sales_tax_percent = 0.07
sales_tax_amount = meal_subtotal * sales_tax_percent

# Calculate the total price of the meal (meal subtotal + tip + sales tax)
total_price = meal_subtotal + tip_amount + sales_tax_amount

# Display the tip amount, sales tax amount, and total price of the meal
print('Meal Subtotal: ${:.2f}, Tip (18%): ${:.2f}, Tax (7%): ${:.2f}, Total: ${:.2f}'
      .format(meal_subtotal, tip_amount, sales_tax_amount, total_price))