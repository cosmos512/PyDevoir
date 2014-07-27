# Write a program with a loop that asks the user to enter a series of
# positive numbers. The user should enter a negative number to signal
# the end of the series. After all the positive numbers have been
# entered, the program should display their sum.

def main():
    print('Enter a positive number or')
    print('enter a negative number to end.')    

    number = int(input('Enter number: '))
    total = 0

    while number >= 0:
        total += number
        print('Enter a positive number or')
        print('enter a negative number to end.')
        number = int(input('Enter number: '))

    print('Total:', total)
    
# Call main function
main()
