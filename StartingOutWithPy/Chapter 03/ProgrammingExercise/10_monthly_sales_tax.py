# A retail company must file a monthly sales tax report listing the total sales
# for the month, and the amount of state and county sales tax collected. The
# state sales tax rate is 4 percent and the county sales tax rate is 2 percent.
# Write a program that asks the user to enter the total sales for the month.
# From this figure, the application should calculate and display the following:
#
#• The amount of county sales tax
#• The amount of state sales tax
#• The total sales tax (county plus state)

STATE_TAX = 0.04
COUNTY_TAX = 0.02

def main():
    total_sales = float(input('Enter amount of total sales for the month: '))
    calculate_tax(total_sales)

def calculate_tax(sales):
    state = sales * STATE_TAX
    county = sales * COUNTY_TAX
    total = state + county
    print(' State tax: $', format(state, '5,.2f'), sep='')
    print('County tax: $', format(county, '5,.2f'), sep='')
    print(' Total tax: $', format(total, '5,.2f'), sep='')

main()
