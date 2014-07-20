# Write a program that converts Celsius temperatures to Fahrenheit temperatures.
# The formula is as follows:
#         9
#     F = - C + 32
#         5
# The program should ask the user to enter a temperature in Celsius, and then
# display the temperature converted to Fahrenheit.

C = float(input('What is the Celsius temperature you saw?: '))

F = 9 / 5 * C + 32

print("Well, then that means it's", format(F, '.1f'), "degrees Fahrenheit.")
