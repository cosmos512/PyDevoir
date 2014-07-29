# The following formula can be used to determine the distance an object falls
# due to gravity in a specific time period, starting from rest:
#
#           d = (1/2) * g * t^2
#
# The variables in the formula are as follows: d is the distance in meters,
# g is 9.8, and t is the amount of time in seconds, that the object has been
# falling. Write a function named falling_distance that accepts an object’s
# falling time in seconds as an argument. The function should return the
# distance in meters that the object has fallen during that time interval.
# Write a program that calls the function in a loop that passes the values 1
# through 10 as arguments and displays the return value.

# Global constant (gravity?)
G = 9.8

def main():
    print('Time [Secs]\tFalling Distance [M]')
    print('------------------------------------')
    for t in range(1, 11):
        distance = falling_distance(t)
        print(t, '\t\t', format(distance, '6.2f'))

def falling_distance(t):
    d = (1/2) * G * t**2
    return d

main()
