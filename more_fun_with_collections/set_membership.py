"""
Program: set_membership.py
Author: Ghulam Omar
This program is an example of function accept a set and return a boolean.
 """

d = {1, 1, 2, 3, 4}  # defining a set.


def in_set(my_set):
    """"accept a set and return a boolean"""
    for i in my_set:
        return 5 in my_set  # returning true or fals.


if __name__ == '__main__':
    print(in_set({0, 1, 2, 3, 4}))
    """" calling the function"""
