# Create a change-counting game that gets the user to enter the number of coins
# required to make exactly one dollar. The program should prompt the user to
# enter the number of pennies, nickels, dimes, and quarters. If the total value
# of the coins entered is equal to one dollar, the program should congratulate
# the user for winning the game. Otherwise, the program should display a
# message indicating whether the amount entered was more than or less than one
# dollar.

def main():
    print('This is the change counting game!')
    print('It\'s not dumb, I swear.')

    # Prompt
    penny = int(input('Enter a number of pennies: '))
    nickel = int(input('Enter a number of nickels: '))
    dime = int(input('Enter a number of dimes: '))
    quarter = int(input('Enter a number of quarters: '))

    # Calculate
    p = penny * 0.01
    n = nickel * 0.05
    d = dime * 0.10
    q = quarter * 0.25
    change = p + n + d + q

    # Decide
    if change == 1.0:
        print('You win! Your change is exactly a dollar!')
    elif change > 1.0:
        print('You lose... Your change is more than a dollar.')
    else:
        print('You lose... Your change is less than a dollar.')

main()
