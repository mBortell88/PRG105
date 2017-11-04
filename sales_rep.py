# use the employee_data class

import employee_data


def main():
    # creating object of the employee_data class - using subclass Prod_worker
    sales_rep = employee_data.Prod_worker('Joe MacMillan', 'JM1982', 1, 100000)

    # print the information

    print("-----Employee Information------")
    print(sales_rep)

# call the main function
main()
