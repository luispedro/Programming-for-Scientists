from pylab import *
from numpy.random import random, seed
seed(1234)
def d2(x,y):
    return exp(-maximum(x**2,y**2))
def P(x,y):
    return .8*d2(x,y)*exp(-x**2-y**2)

X, Y = meshgrid(linspace(-1,1,1000),linspace(-1,1,1000))

xs = [(0.,0.)]
iters = int(1e6)
for i in xrange(iters):
    next = (xs[-1][0] + normal(scale=.1),xs[-1][1] + normal(scale=.1))
    a = random()
    if a < P(*next)/P(*xs[-1]):
        xs.append(next)
    else:
        xs.append(xs[-1])
        
xs = array(xs).T
contour(X,Y,.8*d2(X,Y)*exp(-X**2-Y**2))
savefig('generated/10-complexcontour.pdf')
plot(xs[0][::1000],xs[1][::1000],'rx')
savefig('generated/10-complexcontour-samples.pdf')
