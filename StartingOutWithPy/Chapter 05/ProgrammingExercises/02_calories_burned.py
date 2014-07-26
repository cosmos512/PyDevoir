# Running on a particular treadmill you burn 3.9 calories per minute.
# Write a program that uses a loop to display the number of calories burned
# after 10, 15, 20, 25, and 30 minutes.

def main():
    print('Minutes\tCalories Burned')
    print('-----------------------')

    for minutes in range(10, 31, 5):
        calories = 3.9 * minutes
        print(minutes, '\t', calories)

main()
