"""
This program asks the user for inches of rain for a 12 month period
then it displays the inches of rain per month, the average amount of rainfall for 12 months
and the most amount of rain and least amount of rain in the 12 month period.
"""


def main():
    num_months = 12
    index = 0  # variable to hold index
    rainfall = [0] * num_months
    total_rain = 0  # accumulates the total amount of rainfall

    print('Please enter the amount of rainfall for each month:')

    while index < num_months:
        print('For month ', index + 1, ': ')  # use index + 1 because python starts count at 0
        rainfall[index] = float(input())  # set as float for decimals
        index += 1

    count = 0  # initialize count

    while count < num_months:
        print('The total amount of rainfall for month', count + 1, ':', rainfall[count], 'inches')
        total_rain += rainfall[count]
        count += 1

    # Calculate the average rainfall
    average_rainfall = total_rain / num_months
    print('---------------------------------------------------')  # to separate the overall total, average and min/max
    print('The total amount of rainfall for 12 months:', format(total_rain, ',.2f'), 'inches')
    print('The average rainfall for 12 months:', format(average_rainfall, ',.2f'), 'inches')
    print('The least amount of rain in a month was ', min(rainfall), 'inches')
    print('The most amount of rain in a month was ', max(rainfall), 'inches')


main()
