"""Q11.

Create a Iteratr class for givng numbers up to given input values.


e.g. b = IteratorBee(10), returns same.

Create a generator function factors to give factors of input.
def factors(n):
    …………………."""


class Iterator:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for i in Iterator(3, 8):
    print(i)

"""Create a generator function factors to give factors of input.
def factors(n):
"""


def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
