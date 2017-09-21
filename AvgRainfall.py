"""
 This is a program that calculates the average rainfall
 ask the user for the number of years
 ask for the inches of rainfall per month
 display the average rainfall per year
"""

# variables
num_years = int(input('How many years? '))
# initialize accumulator
total = 0.00
for year in range(num_years):
    print('Year number ', year + 1)
    # Get inches of rain per month
    for month in range(1, 13):
        print('Month number', month)
        inches_rainfall = float(input('How many inches of rain for the month? '))
        total += inches_rainfall/12
print('The average rainfall for ', num_years, ' years is ', format(total/num_years, ',.2f'), 'inches.')
