#Make histograms of popular probability distributions using a random number generator
# use matplotlib and numpy

import numpy as np
import matplotlib.pyplot as plot
import seaborn as sns

sns.set(style = "whitegrid")
np.random.seed(34)

fig, axs=plot.subplots(1,3,figsize = (15, 6))
axs[0].hist(np.random.binomial(10, .5, 100000), color = 'red')
axs[0].set_title("Binomial distribution with p=0.5")

axs[1].hist(np.random.randn(100000), color = 'blue')
axs[1].set_title ("Normal Distribution")

axs[2].hist(np.random.poisson(lam = 5, size = 10000), color ='green')
axs[2].set_title ("Poisson distrbution")

plot.show()