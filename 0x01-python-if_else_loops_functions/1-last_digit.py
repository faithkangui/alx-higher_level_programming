#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_num = number % -10
else:
    last_num = number % 10
if last_num > 5:
    print_value = "and is greater than 5"
elif last_num == 0:
    print_value = "and is 0"
elif (last_num < 6) and not 0:
    print_value = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, last_num, print_value))
