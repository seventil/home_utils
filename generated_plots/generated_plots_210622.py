# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:43:52 2022

@author: User
"""

# This import registers the 3D projection, but is otherwise unused.
# from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the mesh in polar coordinates and compute corresponding Z.
r = np.linspace(0, 8, 60)
p = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 60)
R, P = np.meshgrid(r, p)
# Z = ((R**2 - 1)**2)

data_lin2 = np.array([-580, -578, -572, -564, -540, -520, -490, -450, -410,
                      -360, -300, -240, -205, -170, -116, -71, -35, 78, 102,
                      110, 110, 110, 110, 110, 110, 108, 106, 104, 102, 100,
                      95, 90, 85, 80, 75, 70, 65, 60, 55, 50,
                      45, 40, 36, 32, 28, 24, 21, 18, 15, 12,
                      9, 7, 5, 3, 2, -1, 0, 0, 0, 0])
Q = []
for _ in range(60):
    Q.append(data_lin2)
Q = np.array(Q)

# Express the mesh in the cartesian system.
X, Y = R*np.cos(P), R*np.sin(P)

# Plot the surface.
ax.plot_surface(X, Y, Q, cmap=cm.viridis, linewidth=0.2, edgecolor='k')

# Tweak the limits and add latex math labels.
ax.set_zlim(-2500, 1500)
ax.set_xlabel(r'$L_y$, мм')
ax.set_ylabel(r'$L_x$, мм')
ax.set_zlabel(r'$h$, мкм')

plt.show()
