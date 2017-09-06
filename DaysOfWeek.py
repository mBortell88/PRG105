# Write a program asking user to enter a number 1 through 7
# Numbers should display corresponding day of week
# Define variables, format with input request
number = int(input("Enter a number 1 through 7: "))
if number == 1:
    print("Monday")
elif number ==2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
else:
    print("Error! Entered number must be 1 through 7!")
