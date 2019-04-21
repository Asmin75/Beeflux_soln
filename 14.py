"""Q14.
Write a short program that takes as input three integers, a, b, and c, from the console and determines if they can be used in a correct arithmetic formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”"""


a = int(input("Enter first number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))

if(a + b == c):
    print("a+b=c")
elif(a == b - c):
    print("a=b-c")
elif(a * b == c):
    print("a*b=c")
else:
    print("No formula is suitable")