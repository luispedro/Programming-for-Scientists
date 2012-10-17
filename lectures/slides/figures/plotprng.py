from pylab import *
def update(x, a, b):
    return a*x % b
a = 48271
b = 2**31-1
x = 2321
ys = [x]
for i in xrange(128):
    x = update(x, a, b)
    ys.append(x)
plot(ys)
savefig('generated/prnwalk.pdf')
