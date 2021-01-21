import matplotlib
from bayes_opt import BayesianOptimization
import numpy as np
import scipy

import matplotlib.pyplot as plt
from matplotlib import gridspec

def target(x):
    return -1*(1.3*x*x+2.6*x+0.6)

KAPPA = 5
x = np.linspace(-10, 10, 1000)
y = target(x)

plt.plot(x, y)
#plt.show()
bo = BayesianOptimization(target, {'x': (-2, 10)})

bo.maximize(init_points=2, n_iter=0, acq='ucb', kappa=KAPPA)

for i in range(0,200):
   bo.maximize(init_points=0, n_iter=1, kappa=KAPPA)











