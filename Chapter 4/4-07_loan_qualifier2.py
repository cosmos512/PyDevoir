# This program determines wheter a bank customer
# qualifies for a loan.

# Constants for minimum salary and minimum
# years on the job
MIN_SALARY = 30000.0
MIN_YEARS = 2

def main():
    # Get the customer's annual salary.
    salary = float(input('Enter your annual salary: '))

    # Get the number of years on the current job.
    years_on_job = int(input('Enter the number of '+
                             'years employed: '))

    # Determine wheter the customer qualifies.
    if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print('You do not qualify for this loan.')

# Call the main function.
main()

# Note: this is cool, but it does remove the specific
# reasons _why_ you could be disqualified for the loan.