import numpy as np
from matplotlib import pyplot as plt
vs = np.array([
	20,18,30,32,31,22,28,32,33,32,32,31,30,31,32,30,28,30,24,22,22,20,20,20])
x = np.arange(len(vs))
x2 = x + .99
plt.plot(np.array([x,x2]).T.ravel(), np.repeat(vs,2))
plt.plot([0,len(vs)+1], [26,26])
plt.savefig('generated/fastqtrim.pdf')
