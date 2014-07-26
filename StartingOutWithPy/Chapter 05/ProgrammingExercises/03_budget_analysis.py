# Write a program that asks the user to enter the amount that they have
# budgeted for a month. A loop should then prompt the user to enter each of
# their expenses for the month, and keep a running total. When the loop
# finishes, the program should display the amount that the user is over
# or under budget.

def budget():
    # Get the budget's limit.
    m_limit = float(input('Enter amount budgeted for the month: '))

    # Initialize accumulator variable.
    total_expenses = 0.0

    # Variable to control the loop.
    another = 'y'

    # Get each expense and accumulate them.
    while another == 'y' or another == 'Y':
        # Get expense and tack it to the accumulator.
        expense = float(input('Enter expense: '))

        # Validate expense.
        while expense < 0:
            print('ERROR: You can\'t enter a negative amount.')
            expense = float(input('Enter correct expense: '))
        
        total_expenses += expense
        # Do it again?
        another = input('Do you have another expense? ' + \
                        '(Enter y for yes): ')

    # Determine over/under budget's amount.
    if m_limit > total_expenses:
        under = m_limit - total_expenses
        print('You are $', format(under, ',.2f'), ' under budget!', sep='')
    elif m_limit < total_expenses:
        over = total_expenses - m_limit
        print('You are $', format(over, ',.2f'), ' over budget...', sep='')
    else:
        print('Impressively, you are exactly on budget.')

# Call budget function.
budget()
