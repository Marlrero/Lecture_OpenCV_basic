# https://stackoverflow.com/questions/38698277/plot-normal-distribution-in-3d

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal # scipy 패키지 설치해야 함

#Parameters to set
mu_x = 0
variance_x = 3

mu_y = 0
variance_y = 15

#Create grid and multivariate normal
x = np.linspace(-25, 25, 1000)
y = np.linspace(-25, 25, 1000)
X, Y = np.meshgrid(x,y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X; pos[:, :, 1] = Y
rv = multivariate_normal([mu_x, mu_y], [[variance_x, 0], [0, variance_y]])

#Make a 3D plot
fig = plt.figure()
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, rv.pdf(pos), cmap='viridis')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
#ax.clabel(s, fontsize=9, inline=1)
plt.show()