"""
This program calculates the minimum amount of insurance
a customer needs to insure their building or home.
The minimum amount advised is 80% of the full value of the home/building
"""


def full_rep():
    # This function gathers full cost of home/building from user
    print("This program will calculate the minimum amount you will need to insure your home/building.")
    # User's full replacement cost
    rep_cost = float(input("What is the cost of full replacement for your home/building?"))
    min_ins(rep_cost)


def min_ins(rep_cost):
    # This function calculates the minimum amount to insure
    # User's minimum amount to insure, 80% full replacement cost
    min_ins_cost = rep_cost * 0.8
    print("The minimum amount you should insure is $", format(min_ins_cost, ',.2f'))


full_rep()
