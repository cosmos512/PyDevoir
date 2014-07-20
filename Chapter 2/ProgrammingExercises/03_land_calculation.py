# One acre of land is equivalent to 43,560 square feet. Write a program that
# asks the user to enter the total square feet in a tract of land and
# calculates the number of acres in the tract.
# Hint: divide the amount entered by 43,560 to get the number of acres.

total_sq_ft = int(input('What is the total square feet of this tract of land?: '))
acres = total_sq_ft / 43560
print('Well, then your land is', acres, 'acre(s) big.')
