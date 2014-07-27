# One foot equals 12 inches. Write a function named feet_to_inches that
# accepts a number of feet as an argument, and returns the number of inches
# in that many feet. Use the function in a program that prompts the user
# to enter a number of feet and then displays the number of inches in that
# many feet.

def main():
    feet = int(input('Enter a number of feet: '))
    inches = feet_to_inches(feet)
    print('There are', inches, 'inches in', feet, 'feet.')

def feet_to_inches(feet):
    return feet * 12

main()
