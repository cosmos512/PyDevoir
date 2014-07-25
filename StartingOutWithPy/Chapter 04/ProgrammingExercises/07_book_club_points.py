# Serendipity Booksellers has a book club that awards points to its customers
# based on the number of books purchased each month. The points are awarded
# as follows:
#
#• If a customer purchases 0 books, they earns 0 points.
#• If a customer purchases 1 book, they earns 5 points.
#• If a customer purchases 2 books, they earns 15 points.
#• If a customer purchases 3 books, they earns 30 points.
#• If a customer purchases 4 or more books, they earns 60 points.
#
# Write a program that asks the user to enter the number of books that they
# have purchased this month and displays the number of points awarded.

def main():
    # Prompt
    books = int(input('Enter amount of books bought this month: '))

    # Decide (the else will be the no books bought)
    if books == 1:
        print('You\'ve earned 5 points!')
    elif books == 2:
        print('You\'ve earned 15 points!')
    elif books == 3:
        print('You\'ve earned 30 points!')
    elif books >= 4:
        print('You\'ve earned 60 points!')
    else:
        print('You haven\'t bought any books.')

main()
