from numpy.random import seed
from numpy.random import normal
from numpy import savetxt
from numpy import mean
from numpy import std
from matplotlib import pyplot as plt

# define underlying distribution of results
mean = 60
stev = 90
# generate samples from ideal distribution
seed(1)
results = normal(mean, stev, 1000)
# save to ASCII file
savetxt('results3.csv', results)

plt.hist(results)
plt.show()

