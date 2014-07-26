# Write a program that uses nested loops to collect data and calculate the
# average rainfall over a period of years. The program should first ask for
# the number of years. The outer loop will iterate once for each year. The
# inner loop will iterate twelve times, once for each month. Each iteration
# of the inner loop will ask the user for the inches of rainfall for that
# month. After all iterations, the program should display the number of
# months, the total inches of rainfall, and the average rainfall per month
# for the entire period.

def main():
    num_years = int(input('Enter the number of years: '))
    print()

    total_months = 0
    total_rain = 0

    for year in range(num_years):
        print('Year', year + 1)
        print('--------')
        for month in range(1, 13):
            print('Month ', month, ': ', sep='', end='')
            inches = int(input('Inches of rain: '))
            total_months += 1
            total_rain += inches
        print()

    avg_rain = total_rain / total_months

    print()
    print('Results for', total_months, 'months:')
    print('Total inches of rainfall:', total_rain)
    print('Average monthly rainfall:', avg_rain)

main()
