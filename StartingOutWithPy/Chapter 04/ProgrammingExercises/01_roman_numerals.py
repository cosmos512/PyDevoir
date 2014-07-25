# Write a program that prompts the user to enter a number within the
# range of 1 through 10. The program should display the Roman numeral
# version of that number. If the number is outside the range of 1 through
# 10, the program should display an error message.

def main():
    number = int(input('Enter a number from 1 through 10: '))

    if number == 1:
        print('Equivalent roman numeral: I')
    elif number == 2:
        print('Equivalent roman numeral: II')
    elif number == 3:
        print('Equivalent roman numeral: III')
    elif number == 4:
        print('Equivalent roman numeral: IV')
    elif number == 5:
        print('Equivalent roman numeral: V')
    elif number == 6:
        print('Equivalent roman numeral: VI')
    elif number == 7:
        print('Equivalent roman numeral: VII')
    elif number == 8:
        print('Equivalent roman numeral: VIII')
    elif number == 9:
        print('Equivalent roman numeral: IX')
    elif number == 10:
        print('Equivalent roman numeral: X')
    else:
        print('Can\'t read, can you?')

main()
