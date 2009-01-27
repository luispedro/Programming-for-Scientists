    
try:
    x = 0
    y = 1/x
except ArithmeticError:
    print 'f-p error'
except ZeroDivisionError:
    print 'divide by zero error'
except:
    print 'generic error'
    

try:
    x = 0
    y = 1/x
except ArithmeticError:
    print 'arithmetic error'
except ZeroDivisionError:
    print 'divide by zero error'
except:
    print 'generic error'
