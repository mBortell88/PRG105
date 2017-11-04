# The employee_data class holds the basic data for the employee
# It will serve as the superclass


class Employee_data(object):
    # accepts the employee_name & employee_num (employee number) attributes
    # initialize the attributes w/ defining __init__ method
    def __init__(self, employee_name, employee_num):
        self.__employee_name = employee_name
        self.__employee_num = employee_num

    # mutators
    def set__employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set__employee_num(self, employee_num):
        self.__employee_num = employee_num

    # accessors
    def get_employee_name(self):
        return self.__employee_name

    def get_employee_num(self):
        return self.__employee_num

    def __str__(self):
        info = 'Employee Name: ' + self.get_employee_name() + '\n' + 'Employee number: ' + str(self.get_employee_num())
        return info


# create subclass of superclass Employee_data
class Prod_worker(Employee_data):

    # __init__  method accepts arguments employee_name & employee_num.
    # Adds special attributes: shift_num (shift number) & hourly_pay_rate

    def __init__(self, employee_name, employee_num, shift_num, hourly_pay_rate):
        # call the superclass Employee_data, pass arguments self, employee_name & employee_num
        Employee_data.__init__(self, employee_name, employee_num)

        # initialize the special attributes of Prod_worker class
        self.__shift_num = shift_num
        # note: shift_num is based on a 2-shift system, entering 1 = day and 2 = night
        self.__hourly_pay_rate = hourly_pay_rate

    # mutators
    def set__shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set__hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    # accessors
    def get_shift_num(self):
        return self.__shift_num

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    # create __str__ to override parent/superclass __str__ method
    def __str__(self):
        p_worker = 'Employee Name: ' + self.get_employee_name() + '\nEmployee ID Number: ' + str(self.get_employee_num()) + '\nShift Number: ' + str(self.get_shift_num()) + '\nHourly Pay Rate: ' + "${:0,.2f}".format(self.get_hourly_pay_rate())
        return p_worker
