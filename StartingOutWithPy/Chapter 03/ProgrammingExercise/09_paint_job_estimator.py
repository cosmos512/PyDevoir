# A painting company has determined that for every 115 square feet of wall
# space, one gallon of paint and eight hours of labor will be required. The
# company charges $20.00 per hour for labor. Write a program that asks the
# user to enter the square feet of wall space to be painted and the price of
# the paint per gallon. The program should display the following data:
#
# • The number of gallons of paint required
# • The hours of labor required
# • The cost of the paint
# • The labor charges
# • The total cost of the paint job

PER_HOUR = 20.00

def main():
    sq_feet = int(input('Enter square feet of wall space to be painted: '))
    gallon_price = float(input('Enter the cost of paint per gallon: '))
    estimation(sq_feet, gallon_price)

def estimation(sq_feet, gallon_price):
    # • The number of gallons of paint required
    total_paint = sq_feet / 115
    # • The hours of labor required
    hours_labor = total_paint * 8
    # • The cost of the paint
    cost_paint = total_paint * gallon_price
    # • The labor charges
    cost_labor = hours_labor * PER_HOUR
    # • The total cost of the paint job
    cost_total = cost_paint + cost_labor

    print('Gallons of paint required:', format(total_paint, '.0f'))
    print('  Hours of labor required:', format(hours_labor, '.0f'))
    print('Cost of paint: $', format(cost_paint, '10,.2f'), sep='')
    print('Cost of labor: $', format(cost_labor, '10,.2f'), sep='')
    print('   Total cost: $', format(cost_total, '10,.2f'), sep='')

main()
