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


fig = plt.figure(figsize=(4, 4))

ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.set_box_aspect(aspect=(1, 1, 0.2))
ax.view_init(14, 190)


# Create the mesh in polar coordinates and compute corresponding Z.
r = np.linspace(0, 8, 60)
print(r)
p = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 60)
print(p)
R, P = np.meshgrid(r, p)
# Z = ((R**2 - 1)**2)

data_lin = np.array([-50, -55, -75, -98, -125, -166, -195, -223, -268, -317,
                     -354, -405, -445, -430, -360, -290, -220, -150, -75, -32,
                     -10, -55, -100, -150, -200, -250, -298, -296, -290, -282,
                     -274, -260, -240, -220, -200, -180, -160, -142, -126,
                     -112, -100, -90, -81, -73, -65, -58, -52, -46, -41, -36,
                     -32, -28, -24, -21, -18, -16, -14, -12, -10, -6])
Z = []
for _ in range(60):
    Z.append(data_lin)
Z = np.array(Z)

# Express the mesh in the cartesian system.
X, Y = R*np.cos(P), R*np.sin(P)


# Plot the surface.
ax.plot_surface(X, Y, Z, cmap=cm.viridis, linewidth=0.2, edgecolor='k')

# Tweak the limits and add latex math labels.
ax.set_zlim(-450, 0)
ax.set_xlabel(r'$L_y$, мм')
ax.set_ylabel(r'$L_x$, мм')
ax.set_zlabel(r'$\sigma_{xx}$, МПа')

# -----------------------------------------------
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.set_box_aspect(aspect=(1, 1, 0.2))
ax.view_init(4, 185)


data_lin2 = np.array([-580, -578, -568, -560, -548, -532, -488, -460, -428,
                      -392, -352, -308, -258, -204, -144, -80, -12, 32, 92,
                      110, 110, 110, 110, 110, 110, 108, 106, 104, 102, 100,
                      95, 90, 85, 80, 75, 70, 65, 60, 55, 50,
                      45, 40, 36, 32, 28, 24, 21, 18, 15, 12,
                      9, 7, 5, 3, 2, -1, 0, 0, 0, 0])
Q = []
for _ in range(60):
    Q.append(data_lin2)
Q = np.array(Q)

# Express the mesh in the cartesian system.
X2, Y2 = R*np.cos(P), R*np.sin(P)

# Plot the surface.
ax.plot_surface(X2, Y2, Q, cmap=cm.cividis, linewidth=0.2, edgecolor='k')

# Tweak the limits and add latex math labels.
ax.set_zlim(-1000, 400)
ax.set_xlabel(r'$L_y$, мм')
ax.set_ylabel(r'$L_x$, мм')
ax.set_zlabel(r'$h$, мкм')


fig.tight_layout()
plt.show()
