from numpy import *
from pylab import *
X=linspace(0,10,1000)
Yp=sin(X)*(1.-X)
points=Yp+rand(*Yp.shape)-.5
plot(X[::10],points[::10],'rx')
plot(X,Yp)
xlabel('t')
ylabel(r'$\eta(t)$')
grid()
savefig('plot.pdf')

