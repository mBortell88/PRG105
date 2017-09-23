total = 0.00


def total_calories():
    print("This program calculates the total fat, carbs and protein consumed in a day.")
    fat()
    carb()
    protein()
    print("The day's total calories: ", total)


def fat():
    # This function asks the user for the amount of fat calories consumed
    fat_cal = float(input("How many calories of fat (in grams) were consumed?"))
    total_fat = fat_cal * 9
    print("The day's total calories from fat: ", total_fat)
    global total
    total += total_fat


def carb():
    # This function asks the user for the amount of carb calories consumed
    carb_cal = float(input("How many calories of carbs (in grams) were consumed?"))
    total_carb = carb_cal * 4
    print("The day's total calories from carbs: ", total_carb)
    global total
    total += total_carb


def protein():
    # This function asks the user for the amount of protein calories consumed
    protein_cal = float(input("How many calories of proteins (in grams) were consumed?"))
    total_protein = protein_cal * 4
    print("The day's total calories from protein: ", total_protein)
    global total
    total += total_protein


total_calories()
