# Many financial experts advise that property owners should insure their
# homes or buildings for at least 80 percent of the amount it would cost
# to replace the structure. Write a program that asks the user to enter
# the replacement cost of a building and then display the minimum amount
# of insurance he or she should buy for the property.

def main():
    # Find the replacement cost
    cost = float(input('Enter the replacement cost for home or building: '))
    # Find insurance minimum
    insurance(cost)

def insurance(cost):
    min_amount = cost * 0.80
    print('The minimum amount of insurance you should buy is $', \
          format(min_amount, ',.2f'), sep='')

main()
