import numpy as np
from matplotlib import pyplot as plt
X = np.linspace(-4, 4, 100)
Y = np.exp(.5-X*X)
plt.plot(X, Y, 'bo')
plt.plot(X, Y, 'r-')
plt.xlabel(r'$x$')
plt.ylabel(r'$\exp \frac{x^2}{2}$')

plt.savefig('generated/gaussian.pdf')
