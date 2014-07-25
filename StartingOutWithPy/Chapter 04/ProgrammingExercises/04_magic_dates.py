# The date June 10, 1960, is special because when it is written in the
# following format, the month times the day equals the year:
#
# 6/10/60
#
# Design a program that asks the user to enter a month (in numeric form),
# a day, and a two-digit year. The program should then determine whether
# the month times the day equals the year. If so, it should display a
# message saying the date is magic. Otherwise, it should display a message
# saying the date is not magic.

def main():
    # Prompting
    month = int(input('Enter a month (in numeric form): '))
    date = int(input('Enter a date: '))
    year = int(input('Enter a year\'s last two digits: '))

    # Calculate
    number = month * date

    # Break the news
    if number == year:
        print('This date is magic! :)')
    else:
        print('This date is not magic... :(')

main()
