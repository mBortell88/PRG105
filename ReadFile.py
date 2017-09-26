# This is a program that reads, counts and displays
# the names from the name.txt file


def main():
    # Open the file names.txt for reading
    names_file = open('names.txt', 'r')
    # Initialize count to count names in file
    count = 0.00
    print('Here are the names in the file: ')
    # Start loop, will keep reading
    # until reads an empty string
    for name in names_file:
        # Add 1 to count
        count += 1
        # Remove \n from each line
        name = name.rstrip('\n')
        # Display name
        print(name)
    # Close the file
    names_file.close()
    print('There are ', count, ' names in the file.')


# Call the main function
main()
