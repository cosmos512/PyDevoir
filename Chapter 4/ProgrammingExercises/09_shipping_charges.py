# The Fast Freight Shipping Company charges the following rates:
#
#  Weight of Package                                  Rate per Pound
#   2 pounds or less                                   $1.10
#   Over 2 pounds but not more than 6 pounds           $2.20
#   Over 6 pounds but not more than 10 pounds          $3.70
#   Over 10 pounds                                     $3.80
#
# Write a program that asks the user to enter the weight of a package and
# then displays the shipping charges.

def main():
    # Prompt
    weight = float(input('Enter weight of package: '))

    # Decide + Calculate
    if weight <= 2:
        rate = weight * 1.10
        print('Shipping charges: $', format(rate, ',.2f'), sep='')
    elif weight > 2 and weight <= 6:
        rate = weight * 2.20
        print('Shipping charges: $', format(rate, ',.2f'), sep='')
    elif weight > 6 and weight <= 10:
        rate = weight * 3.70
        print('Shipping charges: $', format(rate, ',.2f'), sep='')
    else:
        rate = weight * 3.80
        print('Shipping charges: $', format(rate, ',.2f'), sep='')

main()
