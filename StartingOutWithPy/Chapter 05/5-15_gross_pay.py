# This program displays gross pay.
# This program lets you claim more hours than there are in a decade...

def main():
    # Get the number of hours worked.
    hours = int(input('Enter the hours worked this week: '))

    # Get the hourly pay rate.
    pay_rate = float(input('Enter the hourly pay rate: '))

    # Calculate the gross pay.
    gross_pay = hours * pay_rate

    # Display the gross pay.
    print('Gross pay: $', format(gross_pay, ',.2f'))

# Call the main function.
main()
