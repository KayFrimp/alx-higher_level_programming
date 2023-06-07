#!/usr/bin/python3
def print_last_digit(number):
    str_number = str(number)
    last_str_number = str_number[-1]
    last_digit = int(last_str_number)
    print("{:d}".format(last_digit), end="")
    return last_digit
