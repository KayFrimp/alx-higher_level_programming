#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print("{:d}{:d}".format(number // 10, number % 10))
    else:
        print("{:d}{:d}, ".format(number // 10, number % 10), end="")
