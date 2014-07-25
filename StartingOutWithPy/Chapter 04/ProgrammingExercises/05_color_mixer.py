# The colors red, blue, and yellow are known as the primary colors because
# they cannot be made by mixing other colors. When you mix two primary colors,
# you get a secondary color, as shown here: 
#
# When you mix red and blue, you get purple.
# When you mix red and yellow, you get orange.
# When you mix blue and yellow, you get green.
#
# Design a program that prompts the user to enter the names of two primary
# colors to mix. If the user enters anything other than “red,” “blue,” or
# “yellow,” the program should display an error message. Otherwise, the
# program should display the name of the secondary color that results.

def main():
    # Ask for 2 primary colors
    print('Let\'s mix primary colors!')
    print('Primary colors are red, blue, and yellow.')
    color1 = input('Enter the name of a primary color: ')
    color2 = input('Enter the name of another primary color: ')

    if color1 == 'red' and color2 == 'blue':
        print('Mixing those, you get purple!')  # Best color.
    elif color1 == 'red' and color2 == 'yellow':
        print('Mixing those, you get orange!')
    elif color1 == 'blue' and color2 == 'yellow':
        print('Mixing those, you get green!')
    elif color2 == 'red' and color1 == 'blue':
        print('Mixing those, you get purple!')
    elif color2 == 'red' and color1 == 'yellow':
        print('Mixing those, you get orange!')
    elif color2 == 'blue' and color1 == 'yellow':
        print('Mixing those, you get green!')
    else:
        print('Not a color I asked for...')

main()
