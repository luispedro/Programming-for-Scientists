def xrange_like(stop):
    i = 0
    while i < stop:
        print 'in xrange_like'
        yield i
        i += 1


for val in xrange_like(10):
    print 'val:', val

