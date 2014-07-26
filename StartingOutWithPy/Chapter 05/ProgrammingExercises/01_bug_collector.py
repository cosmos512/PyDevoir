# A bug collector collects bugs every day for seven days. Write a program
# that keeps a running total of the number of bugs collected during the
# seven days. The loop should ask for the number of bugs collected for
# each day, and when the loop is finished, the program should display the
# total number of bugs collected.

def main():
    # Accumulator variable.
    total_bugs = 0

    # Get number of bugs.
    for counter in range(1, 8):
        print('Enter amount of bug for day', counter, end='')
        bugs = int(input(': '))
        # Add bugs to running count.
        total_bugs += bugs

    # Display the total number of bugs.
    print('The total number of bugs collected is', total_bugs)

# Call the main function
main()
