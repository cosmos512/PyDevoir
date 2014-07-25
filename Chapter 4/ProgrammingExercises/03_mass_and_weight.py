# Scientists measure an object’s mass in kilograms and its weight in newtons.
# If you know the amount of mass of an object in kilograms, you can calculate
# its weight in newtons with the following formula:
#
#                  weight = mass * 9.8
#
# Write a program that asks the user to enter an object’s mass, and then
# calculates its weight. If the object weighs more than 1,000 newtons, display
# a message indicating that it is too heavy. If the object weighs less than
# 10 newtons, display a message indicating that it is too light.

def main():
    # Get the object's mass
    mass = float(input('Enter the mass of the object: '))
    # Calculate the weight
    weight = mass * 9.8
    print('This object weights ', format(weight, ',.2f',), \
          ' newtons.', sep='')
    # Decide
    if weight > 1000:
        print('This object is too heavy!')
    if weight < 10:
        print('This object is too light!')

main()

        
