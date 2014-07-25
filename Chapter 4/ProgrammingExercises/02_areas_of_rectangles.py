# The area of a rectangle is the rectangle’s length times its width.
# Write a program that asks for the length and width of two rectangles.
# The program should tell the user which rectangle has the greater area,
# or if the areas are the same.

def main():
    # Ask for the areas
    rectangle1_lenght = int(input('Lenght of rectangle #1: '))
    rectangle1_width = int(input('Width of rectangle #1: '))
    rectangle2_lenght = int(input('Lenght of rectangle #2: '))
    rectangle2_width = int(input('Width of rectangle #2: '))

    # Calculate surface areas
    rectangle1 = rectangle1_lenght * rectangle1_width
    rectangle2 = rectangle2_lenght * rectangle2_width

    # Compare
    if rectangle1 > rectangle2:
        print('Rectangle #1 has a larger surface area!')
    elif rectangle1 < rectangle2:
        print('Rectangle #2 has a larger surface area!')
    else:
        print('Rectangle #1 and #2 have the same surface ares!')

main()
