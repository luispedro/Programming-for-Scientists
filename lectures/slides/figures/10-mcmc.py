from pylab import *
from numpy import *
X = linspace(-2,2,1000)
def P(x):
    return 1./sqrt(2*pi) * ( 4*.2*exp(-8*x**2)+sqrt(24)*.5*exp(-12*(x-1.)**2)+sqrt(36)*.3*exp(-18*(x+1.)**2) )
random.seed(123)

def mcmc(iters,scale):
    xs = [0.]
    for i in xrange(iters):
        next = xs[-1] + normal(scale=scale)
        a = random.random()
        if a < P(next)/P(xs[-1]):
            xs.append(next)
        else:
            xs.append(xs[-1])
    return xs
xs = mcmc(100000,.1)
plot(X,P(X))
savefig('generated/10-Px.pdf')
hist(xs,len(xs)//10,normed=True)
savefig('generated/10-Px-hist.pdf')

clf()
xs = mcmc(10000,.01)
plot(X,P(X))
hist(xs,len(xs)//10,normed=True)
savefig('generated/10-Px-hist-notmixed.pdf')

