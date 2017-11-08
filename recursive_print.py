# This program uses a recursive function to print numbers 1 through n - a number which is chosen by the user


def main():
    # use exception handling in case enter incorrect value
    try:
        # convert numeric data entered into an integer
        n = int(input("Please enter a non-negative integer:"))

        # call the num_list function, passing n variable
        num_print(n)

    except ValueError:
        print("Non-numeric or negative number was entered. Please enter a non-negative integer.")


# this function will use the recursive approach
def num_print(n):
    count = 0
    while count < n:
        count += 1
        print(count)

# call the main function
main()
