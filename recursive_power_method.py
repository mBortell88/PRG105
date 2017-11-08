# This program uses a recursive function to calculate a number to an exponential power


def main():
    num = 3  # holds integer value
    exponent = 5  # holds exponent value
    #  call the exponent power - e_power function
    e_power(exponent, num)


def e_power(exponent, num):
    # recursive function to calculate exponential powers of num
    count = 0  # hold number of loops
    answer = num  # set equal to num
    while count < exponent - 1:  # subtract one from exponent as the first already accounted for in answer
        answer *= num
        count += 1
    print(answer)

# call the main function
main()
