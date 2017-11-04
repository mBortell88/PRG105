# use the employee_data class

import employee_data


def main():
    # creating object of the employee_data class - using subclass Prod_worker
    name = input("Enter Employee Name: ")
    num = input("Enter Employee Number: ")
    shift = input("Enter the Shift Number, 1 = Day, 2 = Night: ")
    pay = float(input("Enter hourly pay rate: "))
    employee_info = employee_data.Prod_worker(name, num, shift, pay)

    # print the information
    print()
    print("-----Employee Information------")
    print(employee_info)

# call the main function
main()
