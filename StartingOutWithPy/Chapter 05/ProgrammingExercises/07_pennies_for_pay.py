# Write a program that calculates the amount of money a person would earn
# over a period of time if his or her salary is one penny the first day,
# two pennies the second day, and continues to double each day. The program
# should ask the user for the number of days. Display a table showing what
# the salary was for each day, and then show the total pay at the end of the
# period. The output should be displayed in a dollar amount, not the number
# of pennies.

num_days = int(input('How many days? '))

pennies = 0.00

print()
print('Day\tSalary')
print('--------------')

for days in range(1, num_days+1):
    salary = pennies + 0.01
    print(days, '\t$', format(salary, '4,.2f'))
    pennies += salary

# Why does this even work? I get it, but I don't at the same time...
