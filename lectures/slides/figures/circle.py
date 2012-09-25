import numpy as np
from matplotlib import pyplot as plt

def rcircle():
    while True:
        y = 2*np.random.random()-1
        x = 2*np.random.random()-1
        if x*x+y*y < 1.:
            return y,x

X = np.array([rcircle() for i in xrange(10000)])
plt.plot(X.T[0], X.T[1], 'r,')
plt.gca().set_aspect('equal')
plt.savefig('generated/circle.png')
