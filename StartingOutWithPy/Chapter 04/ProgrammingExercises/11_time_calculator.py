# Write a program that asks the user to enter a number of seconds,
# and works as follows:
#
# • There are 60 seconds in a minute. If the number of seconds entered by the
#   user is greater than or equal to 60, the program should display the number
#   of minutes in that many seconds.
#
# • There are 3,600 seconds in an hour. If the number of seconds entered by
#   the user is greater than or equal to 3,600, the program should display
#   the number of hours in that many seconds.
#
# • There are 86,400 seconds in a day. If the number of seconds entered by
#   the user is greater than or equal to 86,400, the program should display
#   the number of days in that many seconds.

def main():
    # Prompt
    seconds = int(input('Enter an amount of seconds: '))

    # Decide, Calculate
    if seconds > 0 and seconds < 60:
        print('There is less than a minute in', format(seconds, '.0f'), \
              'seconds.')
    elif seconds >= 60 and seconds < 3600:
        minutes = seconds / 60
        print('There is(are)', format(minutes, ',.0f'), 'minute(s) in', \
              format(seconds, '.0f'), 'seconds.')
    elif seconds >= 3600 and seconds < 86400:
        hours = seconds / 3600
        print('There is(are)', format(hours, ',.0f'), 'hour(s) in', \
              format(seconds, '.0f'), 'seconds.')
    elif seconds >= 86400:
        days = seconds / 86400
        print('There is(are)', format(days, ',.0f'), 'day(s) in', \
              format(seconds, '.0f'), 'seconds.')
    else:
        print('There are 0 seconds in 0 seconds.')
        print('Yeah, I know, I was surprised too.')

main()
