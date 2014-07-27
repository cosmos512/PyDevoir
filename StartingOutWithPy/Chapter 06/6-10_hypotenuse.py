# This program calculates the length of a right
# triangle's hypotenuse.
# And not only if you are the very model of a
# major-general.
import math

def main():
    # Get the lenght of the triangle's two sides.
    a = float(input('Enter the length of side A: '))
    b = float(input('Enter the length of side B: '))

    # Calculate the lenght of the hypotenuse.
    c = math.hypot(a, b)

    # Display the lenght of the hypotenuse.
    print('The lenght of the hypotenuse is', c)

# Call the main function.
main()
