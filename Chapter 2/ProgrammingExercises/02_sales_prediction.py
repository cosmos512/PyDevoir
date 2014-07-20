# A company has determined that its annual profit is typically 23 percent
# of total sales. Write a program that asks the user to enter the projected
# amount of total sales, and then displays the profit that will be made
# from that amount.
# Hint: use the value 0.23 to represent 23 percent.

total_sales = float(input('Enter projected amount of total sales: '))

annual_profit = total_sales * 0.23

print('Annual profit for the year will be $', format(annual_profit, ',.2f'), '.', sep='')

