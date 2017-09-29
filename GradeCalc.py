# This program requests 5 test scores from the User to calculate their grade


def main():
    # This function processes the calc_average and determine_grade functions
    # Request five test scores from user
    test_score1 = float(input('Please enter the score for the first test: '))
    test_score2 = float(input('Please enter the score for the second test: '))
    test_score3 = float(input('Please enter the score for the third test: '))
    test_score4 = float(input('Please enter the score for the fourth test: '))
    test_score5 = float(input('Please enter the score for the fifth test: '))
    # Initialize accumulator and call cal_average function
    total_scores = calc_average(test_score1, test_score2, test_score3, test_score4, test_score5)
    # Call the determine_grade function
    determine_grade(total_scores)


def calc_average(score1, score2, score3, score4, score5):
    # This function calculates the average
    test_average = (score1 + score2 + score3 + score4 + score5) / 5
    print("Your average test score was: ", test_average)
    return test_average


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


main()
