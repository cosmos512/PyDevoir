# A car’s miles-per-gallon (MPG) can be calculated with the following formula:
#     MPG  = Miles driven / Gallons of gas used
# Write a program that asks the user for the number of miles driven and
# the gallons of gas used. It should calculate the car’s MPG and display
# the result.

#I don't want it to be super precise, I just want a round number.
miles_driven = int(input('How many miles did you drive?: '))
gas_used = int(input('How many gallons of gas did you consume?: '))

MPG = miles_driven // gas_used

print("Your car's Miles-Per-Gallon is", MPG)
