# This program requests 5 test scores from the User to calculate their grade

# Initialize Accumulator
total = 0.00
# Request five test scores from user
test_score1 = float(input('Please enter the score for the first test: '))
test_score2 = float(input('Please enter the score for the second test: '))
test_score3 = float(input('Please enter the score for the third test: '))
test_score4 = float(input('Please enter the score for the fourth test: '))
test_score5 = float(input('Please enter the score for the fifth test: '))
scores = test_score1, test_score2, test_score3, test_score4, test_score5


def grade():
    # This function processes the calc_average and determine_grade functions
    calc_average()
    determine_grade(total)


def calc_average():
    # This function calculates the average
    tests_total = sum(scores)
    test_average = tests_total / 5
    global total
    total += test_average
    print("Your average test score was: ", total)
    return total


def determine_grade(total):
    # This function determines the grade
    if total >= 90.0:
        letter_grade = 'A'
    elif 80.0 <= total < 90.0:
        letter_grade = 'B'
    elif 70.0 <= total < 80.0:
        letter_grade = 'C'
    elif 60.0 <= total < 70.0:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    print("Your final grade is: ", letter_grade)
    return letter_grade


grade()
