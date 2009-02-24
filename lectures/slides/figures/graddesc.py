from pylab import *
X = linspace(-4,2,1000)
def f(x):
    return x**4+4*x**3-4*x

def f_(x):
    return 4*x**3+12*x**2-4

def f__(x):
    return 12*x**2+24*x

def graddesc(x0):
    Xs = [x0]
    eps = 1e-3
    for i in xrange(1000):
        Xs.append(Xs[-1]-eps*f_(Xs[-1]))
    return np.array(Xs)

def newton(x0):
    Xs = [x0]
    for i in xrange(1000):
        Xs.append(Xs[-1]-f_(Xs[-1])/f__(Xs[-1]))
    return np.array(Xs)

for x0 in (2.,-4.):
    Xs = graddesc(x0)
    for k in [2,10,25,100,1000]:
        clf()
        plot(X,f(X))
        xlabel(r'$x$')
        ylabel(r'$x^4+4x^3-4x$')
        plot(Xs[:k],f(Xs[:k]),'rx')
        savefig('generated/graddesc-x0%s-%s.pdf' % (int(x0),k))
    N = newton(x0)
    clf()
    xlabel(r'$x$')
    ylabel(r'$x^4+4x^3-4x$')
    plot(X,f(X))
    plot(N[:10],f(N[:10]),'rx')
    savefig('generated/newton-x0%s.pdf' % int(x0))
    
    clf()
    plot(f(Xs[:20]),'r')
    plot(f(N[:20]),'g')
    xlabel('iteration')
    ylabel(r'$f(x)$')
    legend(('Gradient Descent','Newton'))
    savefig('generated/newton-vs-gd-x0%s.pdf' % int(x0))

