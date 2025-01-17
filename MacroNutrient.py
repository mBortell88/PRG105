# This is a program that calculates the total calories consumed in the day.
# It also totals the calories from fat, carbs and protein


# global variable, accumulator - totals the calories
total_calories = 0.00


def main():
    # This function totals all calories from fat, carbs and protein
    # Accesses additional functions
    print("This program calculates the total fat, carbs and protein consumed in a day.")
    fat()
    carb()
    protein()
    print("The day's total calories: ", format(total_calories, ",.2f"))


def fat():
    # This function asks the user for the amount of fat calories consumed
    global total_calories
    fat_cal = float(input("How many calories of fat (in grams) were consumed?"))
    total_fat = fat_cal * 9
    print("The day's total calories from fat: ", total_fat)
    total_calories += total_fat


def carb():
    # This function asks the user for the amount of carb calories consumed
    global total_calories
    carb_cal = float(input("How many calories of carbs (in grams) were consumed?"))
    total_carb = carb_cal * 4
    print("The day's total calories from carbs: ", total_carb)
    total_calories += total_carb


def protein():
    # This function asks the user for the amount of protein calories consumed
    global total_calories
    protein_cal = float(input("How many calories of proteins (in grams) were consumed?"))
    total_protein = protein_cal * 4
    print("The day's total calories from protein: ", total_protein)
    total_calories += total_protein


main()
