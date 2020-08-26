import plotly.plotly as py
import plotly.tools as tls

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

fig = plt.figure()

# example data
mu = 100 # mean of distribution
sigma = 15 # standard deviation of distribution
x = mu + sigma * np.random.randn(10000)

num_bins = 50
# the histogram of the data
n, bins, patches = plt.hist(x,num_bins, normed=1, facecolor='green', alpha=0.5)
# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins,y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')

#Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)

plotly_fig = tls.mpl_to_plotly(fig)
py.iplot(plotly_fig, filename='histogram-mpl-legend')
