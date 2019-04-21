"""﻿Q1.
Create a function to sum Input Numbers (parameters) which returns sum of inputed numbers. Also write Unittest for the function.

my_sum(1,2)    should return 3 e.g.
my_sum(1,2,3) should return 6
my_sum(1,3,5,7,8) = ?"""


def my_sum(*args):
    total = 0
    for num in args:
        total += num
    return total


def unittest():
    print(my_sum(1, 3, 5, 7, 8))

unittest()