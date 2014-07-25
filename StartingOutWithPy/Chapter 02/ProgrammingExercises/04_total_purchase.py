# A customer in a store is purchasing five items. Write a program that asks
# for the price of each item, and then displays the subtotal of the sale,
# the amount of sales tax, and the total.
# Assume the sales tax is 6 percent.

item1 = float(input('Price of item one?: '))
item2 = float(input('Price of item two?: '))
item3 = float(input('Price of item three?: '))
item4 = float(input('Price of item four?: '))
item5 = float(input('Price of item five?: '))

subtotal = item1 + item2 + item3 + item4 + item5
sales_tax = subtotal * 0.06
total = subtotal + sales_tax

print(' Subtotal: $', format(subtotal, '10,.2f'))
print('Sales Tax: $', format(sales_tax, '10,.2f'))
print('    Total: $', format(total, '10,.2f'))
