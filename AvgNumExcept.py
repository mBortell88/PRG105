"""This program will count the number of numbers and
calculate the average of the numbers in the
numbers.txt file and display the results.
This has been modified to include exception handling"""


# Define num_avg function

def num_avg():
    try:
        # open the numbers.txt file as a read file
        num_file = open(r'C:\Users\Maggie\PycharmProjects\AverageNumbers\numbers.txt', 'r')
        # initialize the accumulator to calculate the sum
        total = 0.00
        # Initialize count the number of numbers
        count = 0.00
        # start loop to get numbers from file
        for num in num_file:
            # convert string type to integer type
            num_int = int(num)
            # add 1 to count
            count += 1
            # add converted integer to total
            total += num_int
        # close num_file
        num_file.close()
        avg_total = total / count
        # display the total number of integers in file
        print('There were a total of: ', count, 'numbers.')
        # display the average total
        print('The average of the numbers equal: ', format(avg_total, ',.2f'))
    # exception handles if file cannot be accessed or read
    except IOError:
        print('An error occurred trying to read the file!')
    # exception handles if a string value cannot convert to integer
    except ValueError:
        print('Non-numeric data found in file!')

# Call the num_avg function
num_avg()
