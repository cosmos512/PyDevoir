# Programming Exercise #6 in Chapter 2 was the Sales Tax program. For that
# exercise you were asked to write a program that calculates and displays
# the county and state sales tax on a purchase. If you have already written
# that program, redesign it so the subtasks are in functions. If you have
# not already written that program, write it using functions.

def main():
    print('Welcome to the tax calculator!')
    price = float(input('Enter amount of purchase: '))
    print()
    calculate(price)

def calculate(price):
    state_tax = price * 0.02
    county_tax = price * 0.04
    total_tax = state_tax + county_tax
    total_price = price + state_tax + county_tax

    print('  State Tax: $', format(state_tax, '10,.2f'))
    print(' County Tax: $', format(county_tax, '10,.2f'))
    print('  Total Tax: $', format(total_tax, '10,.2f'))
    print('Total Price: $', format(total_price, '10,.2f'))

main()
