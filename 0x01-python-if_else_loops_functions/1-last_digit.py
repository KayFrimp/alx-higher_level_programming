#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_number = str(number)
last_str_number = str_number[-1]
last_number = int(last_str_number)
if number < 0:
    last_number = -last_number
print(f"Last digit of {number:d} is {last_number:d}", end=" ")
if last_number > 5:
    print("and is greater than 5")
elif last_number == 0:
    print("and is 0")
elif last_number < 6 and last_number != 0:
    print("and is less than 6 and not 0")
