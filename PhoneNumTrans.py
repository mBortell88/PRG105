# This program takes an alpha and numeric phone number and converts the
# whole phone number into numeric


# This function processes the input number and translates it
def main():
    print("Please enter a 10 digit phone number you would like translated into numeric.")
    print("The format must be XXX-XXX-XXXX.")
    print("As an example: 555-GET-FOOD would be the necessary format")
    input_phone_num = input("Phone number to translate: ")

    # create an empty list to set input_phone_num to
    phone_num = []
    phone_num += input_phone_num

    # create an empty list to add translated numeric characters to
    numeric_phone_num = []

    # Use for loop to iterate through characters in phone_num
    # ch stands for character
    for ch in phone_num:
            if ch == 'A' or ch == 'B' or ch == 'C':
                numeric_phone_num += '2'
            elif ch == 'D' or ch == 'E' or ch == 'F':
                numeric_phone_num += '3'
            elif ch == 'G' or ch == 'H' or ch == 'I':
                numeric_phone_num += '4'
            elif ch == 'J' or ch == 'K' or ch == 'L':
                numeric_phone_num += '5'
            elif ch == 'M' or ch == 'N' or ch == 'O':
                numeric_phone_num += '6'
            elif ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
                numeric_phone_num += '7'
            elif ch == 'T' or ch == 'U' or ch == 'V':
                numeric_phone_num += '8'
            elif ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'Z':
                numeric_phone_num += '9'
            # set an else in case there are characters other than alphabetic characters
            else:
                numeric_phone_num += ch

    # Join the separated list strings into one
    trans_phone = ''.join(numeric_phone_num)
    # Print results, one showing the original input and one showing the translation
    print("The phone number,", input_phone_num, ",can be translated to:")
    print(trans_phone)


# Call the function
main()
