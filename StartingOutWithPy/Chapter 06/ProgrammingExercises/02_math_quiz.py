# Write a program that gives simple math quizzes. The program should display
# two random numbers that are to be added, such as:
#   247
# + 129
# The program should allow the student to enter the answer. If the answer is
# correct, a message of congratulations should be displayed. If the answer is
# incorrect, a message showing the correct answer should be displayed.
import random

def main():
    print('Let\'s add numbers!')
    print('What is the sum of...')
    
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    total = num1 + num2

    print(num1, '+', num2, '?')
    answer = int(input('Type your answer: '))

    if answer == total:
        print('Congratulation, that is the correct answer.')
    else:
        print('Wrong. The right answer is:')
        print(total)

main()
