# Write a function named maximum that accepts two integer values as arguments
# and returns the value that is the greater of the two. For example, if 7 and
# 12 are passed as arguments to the function, the function should return 12.
# Use the function in a program that prompts the user to enter two integer
# values. The program should display the value that is the greater of the two.

def main():
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    biggest = maximum(num1, num2)
    
    print(biggest, 'is the greater number of the two.')
    

def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

main()
