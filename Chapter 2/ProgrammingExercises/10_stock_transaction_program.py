# Last month Joe purchased some stock in Acme Software, Inc. Here are the
# details of the purchase:
#    • The number of shares that Joe purchased was 1,000.
#    • When Joe purchased the stock, he paid $32.87 per share.
#    • Joe paid his stockbroker a commission that amounted to 2 percent of
#      the amount he paid for the stock.
#
# Two weeks later Joe sold the stock. Here are the details of the sale:
#    • The number of shares that Joe sold was 1,000.
#    • He sold the stock for $33.92 per share.
#    • He paid his stockbroker another commission that amounted to 2 percent
#      of the amount he received for the stock.
#
# Write a program that displays the following information:
#   • The amount of money Joe paid for the stock.
#   • The amount of commission Joe paid his broker when he bought the stock.
#   • The amount that Joe sold the stock for.
#   • The amount of commission Joe paid his broker when he sold the stock.
#   • Display the amount of money that Joe had left when he sold the stock
#     and paid his broker (both times). If this amount is positive, then Joe
#     made a profit. If the amount is negative, then Joe lost money.

stock_buy_price = 1000 * 32.87
comm_fee1 = stock_buy_price * 0.02
stock_sell_price = 1000 * 33.92
comm_fee2 = stock_sell_price * 0.02
assets = stock_sell_price - (stock_buy_price + comm_fee1 + comm_fee2)

print('Stocks bought for: $', format(stock_buy_price, '10,.2f'), sep='')
print('   Commission fee: $', format(comm_fee1, '10,.2f'), sep='')
print('  Stocks sold for: $', format(stock_sell_price, '10,.2f'), sep='')
print('   Commission fee: $', format(comm_fee2, '10,.2f'), sep='')
print('   Current assets: $', format(assets, '10,.2f'), sep='')
