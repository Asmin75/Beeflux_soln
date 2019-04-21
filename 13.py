"""Q13.

Write a function to give squareroot of a value if it is int or float, raise an exception otherwise.
def sqt(x):
………."""


def sqrt(n):
    if (isinstance(n, int) or isinstance(n, float)):
        sqt = n ** (1 / 2)
        return sqt
    else:
        try:
            n = int(n) or float(n)
        except ValueError:
            print("not defiend")


print(sqrt(9))

