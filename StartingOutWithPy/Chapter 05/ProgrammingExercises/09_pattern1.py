# Write a program that uses nested loops to draw this pattern:
# *******
# ******
# *****
# ****
# ***
# **
# *

BASE_SIZE = 7

for r in range(BASE_SIZE):
    for c in range(r + 1, 8, 1):
        print('*', end='')
    print()
