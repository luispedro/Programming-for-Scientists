import pylab
import numpy as np
X = np.linspace(-4,+4,1000)
pylab.plot(X,np.exp(-X**2))
pylab.xlabel(r'$x$')
pylab.ylabel(r'$\exp(-x^{2})$')
pylab.savefig('generated/matplotlibexample.pdf')
