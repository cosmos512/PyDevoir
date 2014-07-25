# A county collects property taxes on the assessment value of property,
# which is 60 percent of the property’s actual value. For example, if
# an acre of land is valued at $10,000, its assessment value is $6,000.
# The property tax is then 64¢ for each $100 of the assessment value.
# The tax for the acre assessed at $6,000 will be $38.40. Write a program
# that asks for the actual value of a piece of property and displays the
# assessment value and property tax.

def main():
    value = float(input('Enter the value of the property: '))
    assessment_value = value * 0.60
    property_tax = ( assessment_value / 100 ) * 0.64
    print('Assessment value of property: $', format(assessment_value, \
          ',.2f'), sep='')
    print('Property Tax: $', format(property_tax, ',.2f'), sep='')

main()
