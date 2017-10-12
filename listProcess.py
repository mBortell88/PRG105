"""
This program creates a list of random numbers, asks a user for a number
between 1 and 100, then takes the number and compares to the random number list
then displays the numbers greater than the user's number
"""


def main():
    greater_num(random_num(), user_num())


def random_num():
    #  Creates a list of random numbers, import random for random processes
    import random
    rand_list = []  # empty list to append random numbers to
    index = 0   # variable to hold index
    for rand_num in range(20):
        rand_list.append(random.randint(1, 100))
        index += 1
    return rand_list


def user_num():
    # Asks user for a number between 1 and 100
    input_num = 0
    valid = 'false'
    while valid != 'true':
        try:
            input_num = int(input('Choose a number between 1 and 100: '))  # used int to make string integer
        except ValueError:
            print('Data entered was not numeric.')
        if 0 < input_num < 100:
                    return input_num
                    valid = 'true'
        else:
            print('Error! Number must be between 1 and 100.')


def greater_num(rand_num_list, users_num):
    greatlist2 = []  # empty list to add greater numbers
    var1 = 0  # Variable to accrue value to see if any numbers greater than the user's number
    for x in rand_num_list:  # variable x is elements of list
        if users_num < x:
            greatlist2.append(x)  # Adds numbers greater to new list
    for x in greatlist2:
        if users_num < x:
            var1 += 1
    if var1 > 0:
        print('The following numbers were greater than your number: ', greatlist2)
    else:
        print('No numbers were greater.')
    print(rand_num_list)


main()
