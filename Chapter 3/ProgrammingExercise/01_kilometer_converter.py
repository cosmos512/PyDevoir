# Write a program that asks the user to enter a distance in kilometers,
# and then converts that distance to miles.
# The conversion formula is as follows: Miles = Kilometers * 0.6214
def main():
    km = float(input('Enter distance in kilometers: '))
    converter(km)

def converter(km):
    mi = km * 0.6214
    print('Distance in miles is:', format(mi, ',.4f'))

main()
