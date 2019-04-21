"""
Q15
The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is de- fined as v = p v p 1 +v p 2 +···+v p n . For the special case of p = 2, this results in the traditional Euclidean norm, which represents the length of the vector. For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a Euclidean norm of √ 42 +32 = √16+9 = √ 25 = 5. Give an implementation of a function named norm such that norm(v, p) returns the p-norm value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers."""



def cal(p,*v):
    sum = 0
    for i in v:
        val = i**p
        sum += val
        print(sum**(1/p))


cal(2,4,3)



