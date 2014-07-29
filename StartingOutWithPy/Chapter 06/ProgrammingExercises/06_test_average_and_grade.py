# Write a program that asks the user to enter five test scores. The program
# should display a letter grade for each score and the average test score.
# Write the following functions in the program:
#
#    • calc_average -- This function should accept five test scores as
#      arguments and return the average of the scores.
#
#    • determine_grade -- This function should accept a test score as an
#      argument and return a letter grade for the score, based on the
#      following grading scale:
#
#   Score      LetterGrade
#   90–100          A
#   80–89           B
#   70–79           C
#   60–69           D
#   59-0            F

def main():
    t1 = int(input('Enter test score #1: '))
    t2 = int(input('Enter test score #2: '))
    t3 = int(input('Enter test score #3: '))
    t4 = int(input('Enter test score #4: '))
    t5 = int(input('Enter test score #5: '))
    print()

    for t in [t1, t2, t3, t4, t5]:
        grade = determine_grade(t)
        print('The letter grade is:', grade)
    
    avg = calc_average(t1, t2, t3, t4, t5)
    
    print('The average score is:', format(avg, '.1f')
    
def calc_average(t1, t2, t3, t4, t5):
    return (t1 + t2 + t3 + t4 + t5) / 5

def determine_grade(test):
    if test >= 90 and test <=100:
        return 'A'
    elif test >= 80 and test <= 89:
        return 'B'
    elif test >= 70 and test <= 79:
        return 'C'
    elif test >= 60 and test <= 69:
        return 'D'
    else:
        return 'F'

# Call the main function.
main()
