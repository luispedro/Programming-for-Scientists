import numpy
from pylab import *
X = linspace(-4,2,1000)
def f(x):
    return x**4+4*x**3-4*x

def P(x,T):
    return exp(-T*(4+f(x)))

T = 1.
R = numpy.random.RandomState(123)
def greedy(x0,sigma):
    Rs = [x0]
    for i in xrange(int(1e6)):
        c = Rs[-1] + R.normal(scale=sigma)
        if R.rand() < P(c,T)/P(Rs[-1],T):
            Rs.append(c)
        else:
            Rs.append(Rs[-1])
    return np.array(Rs)


xs = greedy(2,.1)
plot(X,X**4+4*X**3-4*X)
hist(xs[::100],len(xs)//1000,normed=True)
savefig('generated/10-mcmcmin.pdf')
