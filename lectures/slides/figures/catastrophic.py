from pylab import *
def f(x):
    return (1.-cos(x))/(x**2)
X = linspace(-10e-8,10e-8,1000)
plot(X,f(X))
xlabel('x')
ylabel(r'$\frac{1.-\cos x}{x^2}$')
savefig('catastrophic.pdf')

