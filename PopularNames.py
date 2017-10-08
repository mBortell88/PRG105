def main():

    #  Open the file BoyNames.txt
    boy_names_file = open('BoyNames.txt', 'r')
    boys_names = boy_names_file.readlines()
    # close the boy_names_file
    boy_names_file.close()
    # strip the new line character
    index = 0
    while index < len(boys_names):
        boys_names[index] = boys_names[index].rstrip('\n')
        index += 1

    #  Open the file GirlNames.txt
    girl_names_file = open('GirlNames.txt', 'r')
    girls_names = girl_names_file.readlines()
    # close the girl_names_file
    girl_names_file.close()
    # strip the new line character
    index = 0
    while index < len(girls_names):
        girls_names[index] = girls_names[index].rstrip('\n')
        index += 1

    # Combine both boys_names & girls_names lists
    popular_names = boys_names + girls_names

    # Ask user for a name to check against the popular names list
    name = input('Please enter a name to see if it is on the popular name list:')

    if name in popular_names:
        print(name, 'is one of the names on the popular name list.')
    else:
        print('Your name was not on the popular names list.')


main()
