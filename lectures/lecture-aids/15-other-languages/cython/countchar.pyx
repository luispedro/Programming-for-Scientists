def countchar(str,ch):
    res = 0
    for c in str:
        if c == ch:
            res += 1
    return res

def untyped_factorial(n):
    res = 1.
    for i in range(1,n):
        res *= i
    return res

def factorial(int n):
    cdef double res = 1.
    cdef int i
    for i in range(1,n):
        res *= i
    return res
