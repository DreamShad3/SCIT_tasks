from pandas import DataFrame
from pandas import read_csv
from numpy import mean
from matplotlib import pyplot
import numpy
# load results file
results = read_csv('results_poisson.csv', header=None)
values = results.values
final_mean = mean(values)
# collect cumulative stats
means = list()
for i in range(1,101):
	data = values[0:i, 0]
	mean_rmse = mean(data)
	means.append(mean_rmse)
# line plot of cumulative values
pyplot.plot(means)
pyplot.plot([final_mean for x in range(len(means))])
pyplot.show()