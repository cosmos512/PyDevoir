# Write a program that calculates the total amount of a meal purchased at a
# restaurant. The program should ask the user to enter the charge for the
# food, and then calculate the amount of a 15 percent tip and 7 percent sales
# tax. Display each of these amounts and the total.

meal = float(input('How much did your meal cost?: '))
tip = meal * 0.15
tax = meal * 0.07
total = meal + tip + tax

print(' Meal: $', format(meal, '10,.2f'))
print('  Tip: $', format(tip, '10,.2f'))
print('  Tax: $', format(tax, '10,.2f'))
print('Total: $', format(total, '10,.2f'))
