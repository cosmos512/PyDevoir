# A nutritionist who works for a fitness club helps members by evaluating
# their diets. As part of her evaluation, she asks members for the number
# of fat grams and carbohydrate grams that they consumed in a day. Then,
# she calculates the number of calories that result from the fat, using
# the following formula:
#               calories from fat = fat grams * 9
# Next, she calculates the number of calories that result from the
# carbohydrates, using the following formula:
#             calories from carbs = carb grams * 4
# The nutritionist asks you to write a program that will make these
# calculations.

def main():
    # Get input
    fat_cal = int(input('Enter amount of calories from fat: '))
    carb_cal = int(input('Enter amount of calories from carbs: '))

    # Fat calculator
    fat_cal_calc(fat_cal)

    # Carb calculator
    carb_cal_calc(carb_cal)

def fat_cal_calc(fat):
    total = fat * 9
    print('Calories from fat:', total)

def carb_cal_calc(carb):
    total = carb * 4
    print('Calories from carbs:', total)

main()
