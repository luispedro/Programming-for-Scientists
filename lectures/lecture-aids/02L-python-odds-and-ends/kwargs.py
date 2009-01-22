def print_args(arg0,arg1,*args,**kwargs):
    '''
    print_args(arg0,arg1,*args,**kwargs)

    Demonstrates Python's fancy argument passing.
    '''

    print 'Arg 0:', arg0
    print 'Arg 1:', arg1
    print 'Nr Variable Args:', len(args)
    print 'Args:', args
    print 'KwArgs:', kwargs
