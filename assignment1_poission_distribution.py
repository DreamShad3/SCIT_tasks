from numpy.random import seed
import numpy as np
from numpy import savetxt
import matplotlib.pyplot as plt
lam = 30
# generate samples from ideal distribution
seed(1)
results=np.random.poisson(lam, 1000)
# save to ASCII file
savetxt('results_poisson.csv', results)
# histogram
plt.hist(results)
plt.show()

