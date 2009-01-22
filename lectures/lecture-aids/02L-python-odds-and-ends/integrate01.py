def integrate01(f):
    '''
    int_f = integrate01(f)
    ...
    '''
    res = 0.0
    for x in xrange(1000):
        res += f(x/1000.)/1000.
    return res

def identity(x):
    return x

def square(x):
    return x**2


