# use the Office_furniture class

import office_furniture


def main():
    # creating object of the office_furniture class
    swivel_chair = office_furniture.Office_furniture('swivel office chair', 'mesh', 19, 20, 22, 139)

    # print the information
    print("-----Item Description------")

    print('Product: ' + swivel_chair.get_category())
    print('Made of: ' + swivel_chair.get_material())
    print('Length: ' + str(swivel_chair.get_length()))
    print('Width: ' + str(swivel_chair.get_width()))
    print('Height: ' + str(swivel_chair.get_height()))
    print('Price: ' + '${:0,.2f}'.format(swivel_chair.get_price()))

    print(swivel_chair)

# call the main function
main()
