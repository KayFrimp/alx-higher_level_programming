#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for item in my_list:
        if item % 2 == 0:
            new_list.append(1)
        else:
            new_list.append(0)
    return new_list
