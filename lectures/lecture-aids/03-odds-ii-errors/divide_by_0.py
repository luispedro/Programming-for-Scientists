    
try:
    x = 0
    y = 1/x
except IOError:
    print 'i-o error'
except ArithmeticError:
    print 'arithmetic error'
except ZeroDivisionError:
    print 'divide by zero error'
except:
    print 'generic error'
    

try:
    x = 0
    y = 1/x
except ZeroDivisionError:
    print 'divide by zero error'
except ArithmeticError:
    print 'arithmetic error'
except:
    print 'generic error'
