"""
This program obtains a string from a user
in which it will calculate the letter which
appears most frequently in the text
"""


def main():
    # obtains string from user
    # while receive input from user, set case to lowercase
    words = input("Please enter some words:").lower()
    # create empty list to store letters from words string
    word_list = []
    # create variable word count to hold length of user input words
    word_count = 0
    word_count += len(words)
    word_list += words
    # print(word_list, word_count)  # to test
    # create another empty list to hold the alphabetic characters from make_alphabetic function
    new_list = []
    new_list += make_alphabetic(word_list)
    count_letters(new_list, word_count)


def make_alphabetic(words_list):
    # function separates the alphabetic characters from other characters and puts in new list
    # create empty list to hold alpha characters
    letter_alpha_list = []
    # for loop will iterate through words_list
    for element in words_list:
        if element.isalpha():   # will determine if character is alpha, if ture appends to letter_alpha_list
            letter_alpha_list.append(element)
        else:
            continue  # set as continue as there is nothing to be done with other characters
    # print(letter_alpha_list) # to test
    return letter_alpha_list


def count_letters(word_alpha_list, counter_len):
    # function will determine the most frequent character
    # initialize count for while loop
    count = 0
    while count < counter_len:
        num = 0  # holds number of times letter goes through
        max_letter = ''  # variable for most frequent character
        for letter in word_alpha_list:
            letter_count = 0  # holds number of repeating letters
            for l in word_alpha_list:  # this loop will determine duplicates
                letter_count += letter == l
            if letter_count >= num:  # this loop will compare number times for each letter
                if letter in max_letter:
                    continue  # will continue if letter is already the max
                else:
                    max_letter = letter  # will replace the existing letter with a new determined max number
            else:
                continue
            num = letter_count  # reassign num to letter_count as letter_count holds times letter appeared
        print('The letter which appears most frequent in the text:', max_letter)
        print('The letter appeared', num, 'times.')
        return max_letter, num


main()
