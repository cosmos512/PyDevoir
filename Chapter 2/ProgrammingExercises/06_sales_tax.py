# Write a program that will ask the user to enter the amount of a purchase.
# The program should then compute the state and county sales tax. Assume
# the state sales tax is 4 percent and the county sales tax is 2 percent.
# The program should display the amount of the purchase, the state sales tax,
# the county sales tax, the total sales tax, and the total of the sale
# (which is the sum of the amount of purchase plus the total sales tax).

# Hint: use the value 0.02 to represent 2 percent,
# and 0.04 to represent 4 percent.

print('Welcome to the tax calculator!')
price = float(input('Enter amount of purchase: '))
print()

state_tax = price * 0.02
county_tax = price * 0.04
total_tax = state_tax + county_tax
total_price = price + state_tax + county_tax

print('  State Tax: $', format(state_tax, '10,.2f'))
print(' County Tax: $', format(county_tax, '10,.2f'))
print('  Total Tax: $', format(total_tax, '10,.2f'))
print('Total Price: $', format(total_price, '10,.2f'))
