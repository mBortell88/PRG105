"""
This program keeps names and email addresses in a dictionary as key-value pairs.
There is a menu that displays options for the user:
LOOK-UP, ADD, CHANGE, DELETE & QUIT
The program pickles and unpickles the dictionary,
accessing it from the file each time it starts and
saving any altercations to a file when user exits program
"""

# Begin with import pickle
import pickle

# Global constants for menu options
LOOK_UP = 1  # looks up email contacts
ADD = 2      # adds new email/name to contacts
CHANGE = 3   # changes/updates contact email
DELETE = 4   # deletes email/name from contacts
QUIT = 5     # exits and saves changes in program


def main():
    # this function acts as the menu
    # use try/except for handling if file cannot be accessed
    try:
        # open the directory file and set to variable
        input_file = open("directory.dat", 'rb')
        directory = pickle.load(input_file)  # accesses contents from file
    # use the IOError for file error
    except IOError:
        print("An error occurred trying to read/access the file.")
        directory = {}  # create empty directory

    # initialize variable for user's selected choice from menu
    choice = 0

    while choice != QUIT:
        # call the main function to get user's choice
        choice = main_menu()
        # set up if/elif/else statements and pass directory variable
        if choice == LOOK_UP:
            look_up_email(directory)
        elif choice == ADD:
            add_name(directory)
        elif choice == CHANGE:
            change_email(directory)
        elif choice == DELETE:
            delete_name(directory)
        elif choice == QUIT:
            save(directory)


# present the menu
def main_menu():
    # print the menu options
    print('-------------------------------------------')
    print("Main Menu")
    print('-------------------------------------------')
    print("1 - Look-up an email")
    print("2- Add a new name and email address")
    print("3 - Change/update an email address")
    print("4 - Delete name and email from contacts")
    print("5 - Quit \n")
    print('-------------------------------------------')

    # Prompt the user to select an option by entering corresponding number
    # format the user choice as an integer
    choice = int(input("Please select a number option from the menu:"))

    # create while loop to error handle if user enters number out of range
    while choice < 1 or choice > 5:
        print("Please enter a valid number choice.")
        # ask user again for choice
        choice = int(input("Please select a number option from the menu:"))
    # return to pass choice variable to main function
    return choice


def look_up_email(directory):
    # this function searches the directory for user,
    # user inputs email to locate
    print("To look-up an email in the directory, "
          "please enter the following information:")
    name = input("Enter name:")
    print(directory.get(name, "Email address not found."))


def add_name(directory):
    # this function creates a new email in the directory,
    # requests name and email from user
    print("To add a new contact to the directory, "
          "please enter the following information:")
    name = input("Enter name:")
    email = input("Enter email address:")
    # check if the information already exists
    if name not in directory:
        directory[name] = email
    else:
        print("The entered information is already in the directory.")


def change_email(directory):
    # this function changes the email assigned to the name
    # requests the user to enter a name to locate the email value
    # if name found, it prompts for new email address
    print("To change/update an email in the directory, "
          "please enter the following information:")
    name = input("Enter name:")
    if name in directory:
        email = input("Please enter the new email address:")
        directory[name] = email
    else:
        print("Name not found")


def delete_name(directory):
    # this function delets a name and email from the directory
    # requests the name from user to delete contact
    print("To delete contact from the directory,"
          "please enter the following information:")
    name = input("Enter name:")
    if name in directory:
        del directory[name]
        print("Name and email deleted.")
    else:
        print("Name not found.")


def save(directory):
    # display confirmation message that information updated.
    print("Your data changes have been updated.")
    # opeh the directory file again for writing and set to variable
    save_file = open("directory.dat", 'wb')
    pickle.dump(directory, save_file)
    save_file.close()


# Call main function
main()
