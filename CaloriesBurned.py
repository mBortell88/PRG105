# This is a program that calculates calories
# burned after running for 10, 15, 20, 25 & 30 minutes

# Variables
# This is the calories burned per min
cal_burn_per_min = 4.2

for num in range(10, 31, 5):
    calories_burned = num * cal_burn_per_min
    print('The calories burned in ', num, ' minutes are: ', calories_burned)
