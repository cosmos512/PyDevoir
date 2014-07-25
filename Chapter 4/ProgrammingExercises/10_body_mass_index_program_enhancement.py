# In programming Exercise #6 in Chapter 3 you were asked to write a program
# that calculates a person’s body mass index (BMI). Recall from that exercise
# that the BMI is often used to determine whether a person is overweight or
# underweight for their height. A person’s BMI is calculated with the formula
#
#    BMI = weight * 703 / height^2
#
# where weight is measured in pounds and height is measured in inches. Enhance
# the program so it displays a message indicating whether the person has
# optimal weight, is underweight, or is overweight. A person’s weight is
# considered to be optimal if his or her BMI is between 18.5 and 25. If the
# BMI is less than 18.5, the person is considered to be underweight. If the
# BMI value is greater than 25, the person is considered to be overweight.

def main():
    # Prompt
    weight = int(input('Enter weight in pounds: '))
    height = int(input('Enter height in inches: '))

    # Calculate
    BMI = weight * 703 / height ** 2

    # Decide
    if BMI < 18.5:
        print('Your BMI is:', format(BMI, '.1f'))
        print('You may be underweight.')
    elif BMI > 25:
        print('Your BMI is:', format(BMI, '.1f'))
        print('You may be overweight.')
    else:
        print('Your BMI is:', format(BMI, '.1f'))
        print('You may have optimal weight.')

main()
