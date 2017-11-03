# use the Office_furniture class

import office_furniture

def main():
    # creating object of the office_furniture class - using subclass Desk
    wooden_desk = office_furniture.Desk('Office desk', 'wood', 30, 60, 29, 229.88, 'right side', 3)

    # print the information

    print("-----Item Description------")

    print('Product: ' + wooden_desk.get_category())
    print('Made of: ' + wooden_desk.get_material())
    print('Number of Drawers: ' + str(wooden_desk.get_num_of_drawers()))
    print('Length: ' + str(wooden_desk.get_length()))
    print('Width: ' + str(wooden_desk.get_width()))
    print('Height: ' + str(wooden_desk.get_height()))
    print('Price: ' + '${:0,.2f}'.format(wooden_desk.get_price()))

    print(wooden_desk)

# call the main function
main()
