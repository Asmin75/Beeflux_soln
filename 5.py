"""consider a function

def aappend(item , lst):
    return lst.append(item)

a = aappend(1, [])
print(a)

b = aappend(2, a)
print(b)

c = aappend(3, [])
print(c)
"""


def append(item,lst):
    return lst.append(item)


a = append(6,[])
print(a)#None

b = append(2,a)
print(b)#AttributeError: 'NoneType' object has no attribute 'append'

c = append(3,[])
print(c)#None