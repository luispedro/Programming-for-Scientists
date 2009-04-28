def countchar(str,ch):
    res = 0
    for c in str:
        if c == ch:
            res += 1
    return res

def factorial(n):
    res = 1.
    for i in xrange(1,n):
        res *= i
    return res
