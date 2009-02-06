def stddev(values):
    '''
    s = stddev(values)

    '''
    assert values, 'stddev: cannot compute stddev of empty list'

    mu = sum(values)/float(len(values))
    S = 0
    for val in values:
        S += (mu-val)**2
    return S/float(len(values))

