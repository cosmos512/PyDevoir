# There are three seating categories at a stadium. For a softball game, Class A
# seats cost $15, Class B seats cost $12, and Class C seats cost $9. Write a
# program that asks how many tickets for each class of seats were sold, and
# then displays the amount of income generated from ticket sales.

def main():
    Class_A = int(input('Enter amount of tickets sold for Class A: '))
    Class_B = int(input('Enter amount of tickets sold for Class B: '))
    Class_C = int(input('Enter amount of tickets sold for Class C: '))
    seat_calc(A=Class_A, B=Class_B, C=Class_C)

def seat_calc(A, B, C):
    cost_a = A * 15
    cost_b = B * 12
    cost_c = C * 9
    income = cost_a + cost_b + cost_c
    print('Income generated: $', format(income, ',.2f'), sep='')

main()

