# A software company sells a package that retails for $99. Quantity discounts
# are given according to the following table:
#
#   Quantity  | Discount
#    10–19    |   20%
#    20–49    |   30%
#    50–99    |   40%
# 100 or more |   50%
#
# Write a program that asks the user to enter the number of packages purchased.
# The program should then display the amount of the discount (if any) and the
# total amount of the purchase after the discount.

def main():
    # Prompt
    nop = int(input('Enter number of packages purchased: '))

    # Decide + Calculate
    if nop > 0 and nop <= 9:
        price = nop * 99.0
        print('No discount apply.')
        print('Total amount of purchase: $', format(price, ',.2f'), \
              sep='')
    elif nop >= 10 and nop <= 19:
        price = nop * 99.0
        discount = price * 0.20
        total = price + discount
        print('Amount of discount: $', format(discount, ',.2f'), \
              sep='')
        print('Total amount of purchase, after discount: $', \
              format(total, ',.2f'), sep='')
    elif nop >= 20 and nop <= 49:
        price = nop * 99.0
        discount = price * 0.30
        total = price + discount
        print('Amount of discount: $', format(discount, ',.2f'), \
              sep='')
        print('Total amount of purchase, after discount: $', \
              format(total, ',.2f'), sep='')        
    elif nop >= 50 and nop <= 99:
        price = nop * 99.0
        discount = price * 0.40
        total = price + discount
        print('Amount of discount: $', format(discount, ',.2f'), \
              sep='')
        print('Total amount of purchase, after discount: $', \
              format(total, ',.2f'), sep='')        
    elif nop >= 100:
        price = nop * 99.0
        discount = price * 0.50
        total = price + discount
        print('Amount of discount: $', format(discount, ',.2f'), \
              sep='')
        print('Total amount of purchase, after discount: $', \
              format(total, ',.2f'), sep='')        
    else:
        print('You did not buy anything.')

main()
