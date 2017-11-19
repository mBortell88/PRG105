class Products_prices:

    def __init__(self, product, prod_description, quantity, price):
        # initialize attributes
        self.__product = product
        self.__prod_description = prod_description
        self.__quantity = quantity
        self.__price = price

    # mutators, pass arguments
    def set__product(self, product):
        self.__product = product

    def set__prod_description(self, prod_description):
        self.__prod_description = prod_description

    def set__quantity(self, quantity):
        self.__quantity = quantity

    def set__price(self, price):
        self.__price = price

    # accessors, returns variable
    def get_product(self):
        return self.__product

    def get_prod_description(self):
        return self.__prod_description

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    # def __str__(self):
        # item = self.__product + '\n' + self.__prod_description + '\n' + str(self.__quantity) + 'lbs \n' + '${:0,.2f}'.format(self.__price)
