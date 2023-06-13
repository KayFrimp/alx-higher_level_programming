#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = None
    for integer in my_list:
        if biggest is None or biggest < integer:
            biggest = integer
    return biggest
