from pylab import *
from numpy.random import random
ps = filter(lambda x: (x[0]**2+x[1]**2 <= 1.),[(2*random()-1,2*random()-1) for i in xrange(10000)])
ps = array(ps).T
plot(ps[0],ps[1],'rx')
savefig('generated/10-circle.pdf')

