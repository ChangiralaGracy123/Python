# Filename: Week-1 Program.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program that calculates the total amount of a meal purchased at a restaurant
# Last changed: 29-01-2024

# Exercise 2: Prompt the user to enter the charge for the food
food_charge = float(input("Enter the charge for the food: $"))


# Calculate tip (20%)
tip = 0.20 * food_charge

# Calculate meal tax (5%)
tax = 0.05 * food_charge

# Calculate total amount
total_amount = food_charge + tip + tax

# Display amounts
print(f"Tip Amount: ${tip:.2f}")
print(f"Meal Tax: ${tax:.2f}")
print(f"Total Amount: ${total_amount:.2f}")

#Output: The program then displays the calculated tip amount, meal tax amount, and the total amount. Each amount is formatted with two decimal places using f-strings.