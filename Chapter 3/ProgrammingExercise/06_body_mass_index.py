# Write a program that calculates and displays a person’s body mass index (BMI).
# The BMI is often used to determine whether a person is overweight or
# underweight for his or her height. A person’s BMI is calculated with the
# following formula:
#                      BMI = weight * 703 / height^2
# where weight is measured in pounds and height is measured in inches.

# BMI usually stops after the first decimal.

def main():
    # Get Weight, Height
    weight = float(input('Enter your weight in pounds: '))
    height = float(input('Enter your height in inches: '))
    # Calculate & Print
    BMI_calculator(weight, height)

def BMI_calculator(weight, height):
    BMI = weight * 703 / height**2
    print('Your BMI is:', format(BMI, '.1f'))

main()
