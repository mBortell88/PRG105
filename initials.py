# This program retrieves the user's full name and prints the person's initials


def main():
    # get user's first name
    first_name = input('Please enter your first name: ')
    # get user's middle name
    middle_name = input('Please enter your middle name: ')
    # get user's last name
    last_name = input('Please enter your last name: ')

    # Get first character of first_name, middle_name and last_name variables
    # Set variables to equal the first index of string
    first = first_name[0]
    middle = middle_name[0]
    last = last_name[0]

    # Set up initials with having periods between first, middle and last
    initials = first + '.' + middle + '.' + last + '.'

    print("Your initials would be:", initials)


main()
