"""Q12.

Write a program to create a flie name bee.txt write “hello bee to it”

write another program to read the contents of bee.txt in uppercase."""

file = open("bee.txt", "a")
file.write("hello bee\n")
file.close()

with open("bee.txt", 'r') as f:
    content = f.read()
    print(content.upper())