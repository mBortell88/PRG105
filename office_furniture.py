# The office furniture class holds the basic information
# for office furniture for sale.
# It will serve as the parent class / superclass for desk


class Office_furniture(object):
    # accepts category, material, length, width, height & price
    # define __init__ method, initialize attributes
    def __init__(self, category, material, length, width, height, price):
        # putting __ in front of variable hides it from other programs
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    # mutators
    def set__category(self, category):
            self.__category = category

    def set__material(self, material):
            self.__material = material

    def set__length(self, length):
            self.__length = length

    def set__width(self, width):
            self.__width = width

    def set__height(self, height):
            self.__height = height

    def set__price(self, price):
        self.__price = price

    # accessors
    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def __str__(self):
        # convert the numbers into strings
        item = self.__category + ' made of ' + self.__material + ' L ' \
               + str(self.__length) + ' inches x W ' + str(self.__width) + ' inches H ' \
               + str(self.__height) + ' inches @ ${:0,.2f}'.format(self.__price)
        return item

# Below is the subclass Desk, it will inherit attributes from the superclass


class Desk(Office_furniture):
    """ __init__  method accepts arguments category, material,
 length, width, height, price.
  Adds special attributes of location of drawers )loc_of_drawers)
and number of drawers (num_of_drawers)"""
    def __init__(self, category, material, length, width, height, price,
                 loc_of_drawers, num_of_drawers):
        # call superclass Office_furniture and pass arguments including self
        Office_furniture.__init__(self, category, material, length, width,                                  height, price)

        # initialize the location of drawers & number of drawers
        self.__loc_of_drawers = loc_of_drawers
        self.__num_of_drawers = num_of_drawers

    # Add mutators for special attributes
    def set_loc_of_drawers(self, loc_of_drawers):
        self.__loc_of_drawers = loc_of_drawers

    def set_num_of_drawers(self, num_of_drawers):
        self.__num_of_drawers = num_of_drawers

    # Add accessors for special attributes
    def get_loc_of_drawers(self):
        return self.__loc_of_drawers

    def get_num_of_drawers(self):
        return self.__num_of_drawers

# create __str__ to override the superclass __str__
    def __str__(self):
        desk_item = self.get_category() + ' made of ' + self.get_material() + ' with ' +\
            str(self.get_num_of_drawers()) + ' drawers located on the ' + \
            self.get_loc_of_drawers() + ' L ' + str(self.get_length()) + ' inches x W ' + \
            str(self.get_width()) + ' inches x H ' + str(self.get_height()) + \
            ' inches @ $ {:0,.2f}'.format(self.get_price())
        return desk_item
