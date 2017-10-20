"""
this program accesses the object class Person_data
it creates 3 instances of the object
and displays a person's name, address, age and phone number
"""

# start by importing object
import person_data


def main():
    # add 3 people's  & create 3 instances
    person_name = "Maggie Bortell"
    person_address = "4123 Wildwood Drive"
    person_age = 29
    phone_number = "815-814-0810"
    person1 = person_data.Person_data(person_name, person_address, person_age, phone_number)

    person2_name = "Katie Bortell"
    person2_address = "4123 Wildwood Drive"
    person2_age = 28
    phone_number2 = "815-814-3904"
    person2 = person_data.Person_data(person2_name, person2_address, person2_age, phone_number2)

    person3_name = "Pat Lundquist"
    person3_address = "17 Winston Drive"
    person3_age = 76
    phone_number3 = "847-399-3598"
    person3 = person_data.Person_data(person3_name, person3_address, person3_age, phone_number3)

    # print the 3 instances
    print("Here is the data entered: \n")

    print("Name:", person1.get_name())
    print("Address:", person1.get_address())
    print("Age:", person1.get_age())
    print("Phone Number:", person1.get_phone(), "\n")

    print("Name:", person2.get_name())
    print("Address:", person2.get_address())
    print("Age:", person2.get_age())
    print("Phone Number:", person2.get_phone(), "\n")

    print("Name:", person3.get_name())
    print("Address:", person3.get_address())
    print("Age:", person3.get_age())
    print("Phone Number:", person3.get_phone())


main()
