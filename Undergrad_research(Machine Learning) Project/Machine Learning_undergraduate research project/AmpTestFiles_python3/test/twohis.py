import plotly.plotly as py
import plotly.tools as tls

import random
import numpy
import matplotlib.pyplot as plt

histogram = plt.figure()
x = [random.gauss(3,1) for _ in range(400)]
y = [random.gauss(4,2) for _ in range(400)]

bins = numpy.linspace(-10, 10, 100)

plt.hist(x, bins, alpha=0.5)
plt.hist(y, bins, alpha=0.5)

plotly_fig = tls.mpl_to_plotly(histogram)
py.iplot(plotly_fig, filename = 'histogram-mpl-same')
