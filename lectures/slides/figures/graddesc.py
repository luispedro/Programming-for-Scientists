from pylab import *
X = linspace(-4,2,1000)
def f(x):
    return x**4+4*x**3-4*x
def f_(x):
    return 4*x**3+12*x**2-4
def graddesc(x0):
    Xs = [x0]
    eps = 1e-3
    for i in xrange(100):
        Xs.append(Xs[-1]-eps*f_(Xs[-1]))
    return np.array(Xs)

for x0 in (2.,-2.):
    Xs = graddesc(x0)
    for k in [2,10,25,100]:
        clf()
        plot(X,f(X))
        plot(Xs[:k],f(Xs[:k]),'rx')
        savefig('graddesc-x0%s-%s.pdf' % (int(x0),k))

