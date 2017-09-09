# This is a program which asks for a user to input an age
# The age that is inputted is classified
# Displays a message if the person is an infant, child, teenager, or adult.

# Variables
# Formatted as float in case of decimal point entries
person_age = float(input("Please enter an age: "))

if person_age <= 1.0:
    print("Infant")
elif 1.0 < person_age < 13.0:
    print("Child")
elif 13.0 <= person_age < 20.0:
    print("Teenager")
else:
    print("Adult")
