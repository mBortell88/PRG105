# This program calculates the monthly cost for owning and operating an automobile


def monthly_expense():
    print("Calculate monthly Auto Expenses")
    # Get User's monthly loan payment
    loan_pmt = float(input("How much is your monthly loan payment?"))
    # Get User's monthly insurance payment
    car_ins = float(input("What is your monthly insurance payment?"))
    # Get User's monthly gas purchases
    gas = float(input("How much was spent this month for gas?"))
    # Get User's monthly car maintenance or repair costs
    car_maint = float(input("How much was spent in car maintenance or repair this month?"))
    # Calculate the monthly cost
    month_cost = loan_pmt + car_ins + gas + car_maint
    # Display the monthly total
    print("You are spending an average of $", format(month_cost, ',.2f'), " per month.")
    year_expense(month_cost)


def year_expense(month_cost):
    # Calculate the year cost by passing month_cost
    year_cost = month_cost * 12
    # Display the annual cost
    print("Your yearly car expenses should be approximately: $", format(year_cost, ',.2f'))


monthly_expense()
