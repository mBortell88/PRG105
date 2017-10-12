# This program takes an alpha and numeric phone number and converts the
# whole phone number into numeric


def main():
    print("Please enter a 10 digit phone number you would like translated into numeric.")
    print("The format must be XXX-XXX-XXXX.")
    print("As an example: 555-GET-FOOD would be the necessary format")
    input_phone_num = input("Phone number to translate: ")

    phone_num = []
    phone_num += input_phone_num

    numeric_phone_num = []

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
            else:
                numeric_phone_num += ch

    trans_phone = ''.join(numeric_phone_num)
    print("The phone number,", input_phone_num, ",can be translated to:")
    print(trans_phone)


main()
