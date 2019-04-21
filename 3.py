"""Q3.
Consider a function

def student(name, roll, age, address):
    print(name, roll, age, address)



a. What would be output of followings
    student(“pratima”, name=”pratima”, 20, 20, 20)
    student(“pratima”, 20, age=25, “kathmandu”)
   student(“pratima”)"""

def student(name, roll, age, address):
    print(name, roll, age, address)


student("pratima",name="pratima",20,20,20) #SyntaxError: positional argument follows keyword argument
student("pratima",20,age=25,"kathmandu"#SyntaxError: positional argument follows keyword argument
student("pratima")#TypeError: student() missing 3 required positional arguments: 'roll', 'age', and 'address'


