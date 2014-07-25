# Write a program that asks the user to enter the monthly costs for the
# following expenses incurred from operating his or her automobile: loan
# payment, insurance, gas, oil, tires, and maintenance. The program should
# then display the total monthly cost of these expenses, and the total
# annual cost of these expenses.

def main():
    # Get input
    lp = float(input('Enter monthly loan payment cost: '))
    ins = float(input('Enter monthly insurance cost: '))
    gas = float(input('Enter monthly gas cost: '))
    oil = float(input('Enter monthly oil cost: '))
    tire = float(input('Enter monthly tire cost: '))
    maint = float(input('Enter monthly maintenance cost: '))
    # Calculate monthly cost
    monthly(lp, ins, gas, oil, tire, maint)
    # Calculate annual cost
    annually(lp, ins, gas, oil, tire, maint)

def monthly(lp, ins, gas, oil, tire, maint):
    cost_monthly = lp + ins + gas + oil + tire + maint
    print('The monthly amount of expenses is $', \
          format(cost_monthly, ',.2f'), sep='')

def annually(lp, ins, gas, oil, tire, maint):
    cost_annually = (lp + ins + gas + oil + tire + maint) * 12
    print('The annual amount of expenses is $', \
          format(cost_annually, ',.2f'), sep='')

main()
