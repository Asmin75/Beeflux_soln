"""
Q6.

def aappend(item , lst=[]):
    lst = []
    return lst.append(item)

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)
"""


def append(item, lst=[]):
    lst = []
    return lst.append(item)


a=append(1, [])
print(a)#None

b = append(2, a)
print(b)#None

c = append(3, [])
print(c)#None