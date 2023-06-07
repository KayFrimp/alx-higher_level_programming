#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if (ord(letter) in range(97, 123)):
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(letter) - num), end="")
    print()
