# This program accepts a list of numbers and calculates the sum of the list with a recursive approach


def main():
    # this function will create num_list and pass as argument to recursive_sum function
    # importing random to create a list of random numbers
    import random
    num_list = []  # empty list to hold numbers
    index = 0  # holds the index
    for n in range(10):  # chose list length to be 10 numbers long
        num_list.append(random.randint(1, 1000))  # chose to have integers 1 through 1000 for num_list
        index += 1
    print(num_list)  # to see the list of numbers
    recursive_sum(num_list)  # passing num_list


def recursive_sum(num_list):
    count = 0  # to hold number of loops
    total = 0  # to hold total of num_list
    while count < 10:
        for n in num_list:
            total += n  # add each element of the list to the total
            count += 1
    print(total)  # to see the total


main()
