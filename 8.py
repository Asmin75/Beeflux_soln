"""Q8.

def aappend(item , lst):
    lst.append(item)
    return lst

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)
Also give reason to all prints in aapend functions."""


def append(item,lst=[]):
    lst.append(item)
    return lst
a=append(1, [])
print(a)#[1]

b = append(2, a)
print(b)#[1,2]

c = append(3, [])
print(c)#[3]