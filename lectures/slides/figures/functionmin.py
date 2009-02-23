from pylab import *
X = linspace(-4,2,1000)
plot(X,X**4+4*X**3-4*X)
savefig('functionmin.pdf')

