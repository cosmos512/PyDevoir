# Write a program that displays a table of the Celsius temperatures 0 through
# 20 and their Fahrenheit equivalents. The formula for converting a temperature
# from Celsius to Fahrenheit is
#              F = (9/5)C + 32
# where F is the Fahrenheit temperature and C is the Celsius temperature. Your
# program must use a loop to display the table.

print('Celsius\tFahrenheit')
print('------------------')

for C in range(21):
    F = (9/5) * C + 32
    print(C, '\t', format(F, '.1f'))
