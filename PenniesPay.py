# This is a program that calculates the amount of money
# a person would earn if he/she were paid one penny
# the first day, 2 on the second
# and doubles each day after.

# variables
end = int(input("How many days (starting with 1) were worked? "))
print('Days\t Pennies')
print('-----------------------------')
# start accumulator for total
total = 0.00
for days in range(1, end+1):
    salary = 0.01
    # equation will reflect 2 to the power of the day's number
    pennies_earned = format((2**days)*salary, ',.2f')
    print(days, '\t', '\t', pennies_earned)
    # duplicated tab to make table align
    total += float(pennies_earned)
# format the total so it rounds two decimals
print('Total earned: ', format(total, ',.2f'))
