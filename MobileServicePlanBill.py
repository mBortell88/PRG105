# Write program that calculates the customer's monthly bill.
# Ask which package the customer has purchased and how many minutes were used.
# Display the total amount due. Use a dollar sign and two decimal places for currency.

# Variables
package_plan = input('Which package are you subscribed to: Package A, Package B or Package C? ')

if package_plan == "Package A":
    max_minutes_per_month = 450
    std_month_bill = 39.99
    over_max_min_fee = 0.45
    mins_used = float(input('How many minutes were used this month?'))
    if mins_used <= max_minutes_per_month:
        print('$', format(std_month_bill, ',.2f'))
    elif mins_used > max_minutes_per_month:
        bill_for_month = std_month_bill + ((mins_used - max_minutes_per_month) * over_max_min_fee)
        print('$', format(bill_for_month, ',.2f'))
elif package_plan == "Package B":
    max_minutes_per_month = 900
    std_month_bill = 59.99
    over_max_min_fee = 0.40
    mins_used = float(input('How many minutes were used this month?'))
    if mins_used <= max_minutes_per_month:
        print('$', format(std_month_bill, ',.2f'))
    elif mins_used > max_minutes_per_month:
        bill_for_month = ((mins_used - max_minutes_per_month) * over_max_min_fee) + std_month_bill
        print('$', format(bill_for_month, ',.2f'))
elif package_plan == "Package C":
    max_minutes_per_month = 'unlimited'
    std_month_bill = 69.99
    over_max_min_fee = 0.00
    mins_used = float(input('How many minutes were used this month?'))
    bill_for_month = (mins_used * over_max_min_fee) + std_month_bill
    print('$', format(bill_for_month, ',.2f'))
else:
    print('Error! Please enter one of the three following packages for further details:'
          ' Package A, Package B or Package C')
