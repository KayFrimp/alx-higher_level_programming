#!/usr/bin/python3
for num_1 in range(0, 9):
    for num_2 in range(num_1, 10):
        if (num_1 == num_2):
            continue
        print("{:d}{:d}".format(num_1, num_2), end="")
        if (num_1 == 8 and num_2 == 9):
            print("")
            continue
        print(",", end=" ")
