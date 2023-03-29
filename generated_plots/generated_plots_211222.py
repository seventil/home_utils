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

l1_1 = [-12, -12, -12, -11.95, -11.9, -11.8, -11.7, -11.6, -11.4, -11.2,
        -11, -10.6, -10.4, -10.1, -9.8, -9.5, -9.1, -8.66, -8, -7.2,
        -6.5, -5.7, -5, -4, -3.2, -2.5, -2, -1.6, -1.3, -1, -0.8,
        -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]
l1_2 = [-400, -350, -290, -240, -210, -180, -156, -130, -110, -92, -76, -60,
        -50, -40, -30, -20, -12, -10, -8, -6, -5, -4, -3, -2, -1, 0, 2,
        4, 6, 8, 12, 16, 22, 30, 34, 38, 41, 46, 50, 53, 57, 62, 64, 69,
        74, 80, 86, 92, 100, 108, 118, 126, 138, 150, 160, 180, 200, 192,
        182, 176
        ]
l1_3 = [-400, -403, -406, -408, -410, -415, -418, -424, -428, -433, -440,
        -450, -460, -468, -479, -489, -500, -510, -521, -530, -541,
        -550, -562, -575, -588, -600, -617, -635, -646, -658, -580,
        -480, -380, -300, -338, -360, -395, -420, -445, -460, -472,
        -480, -470, -450, -430, -400, -368, -330, -285, -240, -202,
        -175, -150, -123, -100, -80, -63, -50, -41, -35
        ]
l2_1 = [-10, -9.9, -9.8, -9.7, -9.53, -9.3, -9.1, -8.93, -8.7, -8.38, -8,
        -7.75, -7.4, -7, -6.65, -6.1, -5.65, -5.2, -4.7, -4.2, -3.7, -3,
        -2.5, -1.9, -1, 0, 1, 0.9, 0.7, 0.5, 0.3, 0.1, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]
l2_2 = [-460, -434, -405, -376, -340, -310, -280, -250, -222, -200, -180, -160,
        -140, -120, -100, -80, -65, -50, -40, -22, -12, 0, 10, 20, 30, 42,
        50, 62, 74, 85, 90, 100, 108, 115, 125, 135, 144, 150, 158, 165,
        172, 180, 188, 194, 200, 205, 208.7, 215, 217, 222, 221, 217, 215,
        209, 201, 195, 188, 180, 169, 160
        ]
l2_3 = [-460, -461, -465, -472, -475, -481, -488, -495, -501, -510, -520, -528,
        -538, -548, -558, -568, -580, -590, -599, -610, -619, -630, -640,
        -652, -665, -679, -688, -610, -490, -420, -380, -384, -389, -396,
        -401, -408, -415, -420, -428, -435, -443, -450, -458, -465, -473,
        -482, -490, -500, -502, -509, -510, -505, -500, -485, -460, -426,
        -380, -340, -300, -265
        ]
l3_1 = [-22, -21.9, -21.2, -20.7, -19.9, -19.2, -18.4, -17.3, -16.3, -15, -14,
        -12.5, -11, -9.5, -7.6, -5, -2, 1, 0.95, 0.9, 0.8, 0.7, 0.6, 0.5,
        0.4, 0.3, 0.25, 0.2, 0.15, 0.12, 0.09, 0.06, 0.03, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]
l3_2 = [-480, -478, -470, -460, -440, -420, -385, -340, -305, -260, -210,
        -160, -100, -50, 0, 50, 80, 90, 88, 86, 80, 75, 70, 69.5, 67, 64.5,
        63.5, 63, 60, 59, 55, 52, 49, 47, 46, 43.5, 42, 39, 37, 35.5, 34, 32,
        31, 29, 28, 27.1, 26, 22.9, 22.8, 21.5, 20, 18.7, 16, 14.7, 13, 12,
        10, 8, 7, 6.15
        ]
l3_3 = [-480, -485, -489, -510, -525, -550, -575, -600, -620, -645, -660,
        -680, -686, -695, -700, -560, -360, -280, -284, -284.5, -288, -292,
        -300, -310, -312, -322, -330, -340, -354, -366, -380, -392, -400,
        -410, -420, -435, -448, -460, -470, -485, -498, -510, -520, -532,
        -544, -554, -560, -552, -532, -510, -480, -445, -400, -350, -270,
        -200, -140, -100, -60, -45
        ]
l4_1 = [-19, -18.95, -18.8, -18.5, -18, -17.2, -16.2, -15.5, -14, -13, -11.5,
        -9.8, -7, -2.6, -0.6, 1, 1.5, 1.3, 1, 0.8, 0.6, 0.5, 0.4, 0.3, 0.2,
        0.1, 0.09, 0.07, 0.06, 0.05, 0.03, 0.01, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]
l4_2 = [-493, -470, -425, -376, -330, -270, -200, -135, -80, -30, 30, 70, 100,
        130, 150, 160, 165, 165, 164.5, 160, 159.5, 156, 152, 150, 147.5,
        145, 142, 138, 133, 130, 125, 120, 118, 114, 111, 108, 105, 101.5,
        100, 95, 90, 88, 81, 78, 72, 69, 65, 61, 59, 54, 52, 50, 45, 40, 38,
        33, 29, 25, 21, 21
        ]
l4_3 = [-493, -505, -520, -540, -570, -597, -640, -675, -700, -730, -770, -795,
        -813, -700, -490, -340, -252, -258, -264, -270, -279, -289, -297,
        -303, -310, -320, -327, -335, -340, -350, -360, -370, -380, -392,
        -404, -417, -430, -440, -450, -460, -475, -483, -495, -505, -518,
        -526, -540, -550, -560, -567, -572, -571, -552, -505, -460, -420,
        -380, -340, -300, -265
        ]
l5_1 = [-24, -23.7, -23.4, -23.2, -22.8, -22, -21.4, -21, -20.6, -20.3,
        -19.6, -19, -18.4, -17.6, -16.8, -16, -15, -14, -12.6, -11.6,
        -10.4, -9, -7, -5.2, -4, -3, -2.4, -1.6, -1, -0.6, -0.4, -0.3,
        -0.2, -0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0
        ]
l5_2 = [-210, -206, -200, -192, -180, -162, -140, -112, -78, -40, -18, 12,
        38, 60, 76, 90, 96, 100, 99, 98, 96, 94, 92, 90, 88, 86, 84, 80,
        78, 76, 74, 71, 68, 65, 63, 61, 59, 57, 55, 53, 51, 49, 47, 45,
        43, 41, 39, 37, 35, 33, 30, 28, 26, 24, 22, 21, 20, 19, 18, 17
        ]
l5_3 = [-210, -214, -222, -230, -238, -246, -252, -260, -268, -276, -284,
        -290, -294, -298, -300, -294, -280, -260, -254, -250, -249,
        -245, -244, -241, -237, -234, -228, -222, -214, -202, -188,
        -176, -160, -146, -130, -120, -110, -100, -92, -86, -78,
        -72, -66, -62, -56, -52, -50, -46, -42, -39, -35, -32, -29,
        -26, -24, -22, -20, -19, -18, -17
        ]
l6_1 = [-25.5, -25.4, -25.3, -25.1, -24.8, -24.6, -24.2, -23.8, -23.2, -22.8,
        -22, -21.6, -20.8, -20, -19, -18, -16.8, -15, -13.6, -12, -10.8,
        -9, -7, -5.2, -4, -3, -2.4, -1.6, -1, -0.6, -0.4, -0.3, -0.2,
        -0.1, -0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0
        ]
l6_2 = [-236, -235, -232, -228, -222, -216, -208, -198, -184, -174, -160, -146,
        -130, -110, -90, -70, -54, -34, -14, 0, 24, 38, 56, 68, 80, 88,
        96, 102, 110, 116, 120, 122, 121, 120, 112, 104, 98, 93, 87, 78,
        74, 66, 59, 54, 48, 40, 37, 34, 30, 25, 22, 20, 18, 17, 16, 15,
        14, 13, 13, 12
        ]
l6_3 = [-236, -237, -238, -239, -240, -242, -244, -246, -248, -250, -255,
        -256, -260, -264, -267, -270, -273, -276, -280, -284, -288, -292, -296,
        -300, -302, -308, -310, -314, -316, -318, -319, -320, -316, -308, -296,
        -280, -260, -240, -220, -192, -169, -150, -130, -112, -100, -80, -64,
        -56, -46, -42, -40, -38, -36, -34, -32, -30, -29, -28, -27, -26
        ]
l7_1 = [-60, -59.8, -59.6, -59, -58, -57, -56.2, -55, -54, -53, -51.5, -50.5,
        -49, -48, -46, -45, -43, -41, -39, -37, -34, -32, -30, -27,
        -24, -20, -17, -14, -10, -8, -6, -4, -3, -2.4, -1.6, -1,
        -0.6, -0.4, -0.3, -0.2, -0.1, 0, -0.2, -0.1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]
l7_2 = [-245, -244, -242, -240, -236, -230, -226, -220, -216, -208, -200, -192,
        -184, -174, -166, -154, -144, -132, -124, -114, -100, -89, -76, -62,
        -48, -34, -16, 0, 14, 30, 52, 74, 87, 102, 112, 120, 124, 128, 130,
        129, 128, 125, 121, 116, 110, 104, 96, 88, 80, 74, 68, 60, 54, 50, 47,
        43, 41, 40, 39, 38
        ]
l7_3 = [-245, -246, -248, -252, -256, -260, -266, -272, -280, -286, -296, -308,
        -318, -330, -340, -350, -360, -368, -376, -382, -386, -392, -396, -399,
        -400, -399, -396, -390, -384, -374, -362, -350, -342, -330, -320, -312,
        -308, -303, -300, -298, -296, -293, -290, -286, -280, -272, -264, -250,
        -238, -224, -212, -200, -186, -175, -164, -156, -148, -140, -134, -128
        ]
l8_1 = [-54, -53.8, -53.6, -53.4, -53.2, -53, -52.4, -51.8, -51, -50, -49, -48,
        -46.4, -45.4, -44, -42, -40, -38, -36, -34, -31, -28, -25, -22,
        -19, -16, -13, -10, -7.4, -6, -4, -2.4, -1.6, -1, -0.6, -0.4,
        -0.3, -0.2, -0.1, 0, -0.2, -0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0
        ]
l8_2 = [-267, -266, -264, -262, -260, -256, -253, -249, -244, -238, -232,
        -224, -212, -202, -190, -172, -158, -140, -116, -92, -69, -48, -28,
        -8, 12, 28, 50, 66, 82, 96, 108, 117, 126, 132, 134, 135, 133, 131,
        126, 118, 108, 100, 92, 84, 77, 70, 64, 59, 56, 54, 51, 50, 49, 48,
        47, 46, 45, 44, 43, 42
        ]
l8_3 = [-267, -267.4, -268, -270, -273, -274, -278, -283, -286, -292, -296,
        -300, -308, -316, -325, -333, -341, -350, -356, -362, -368, -372, -376,
        -379, -380, -380.6, -381, -380, -373, -364, -350, -336, -312, -286,
        -272, -270, -268, -258, -246, -232, -216, -200, -186, -174, -160,
        -146, -134, -124, -114, -107, -100, -94, -90, -86, -83, -80,
        -77.5, -74, -72, -70,
        ]
# (max_x, min_y, max_y, min_z)
r1 = (300, -700, 200, l1_1[0])
r2 = (380, -700, 250, l2_1[0])
r3 = (780, -700, 100, l3_1[0])
r4 = (780, -900, 200, l4_1[0])
r5 = (480, -300, 100, l5_1[0])
r6 = (480, -350, 150, l6_1[0])
r7 = (600, -400, 150, l7_1[0])
r8 = (600, -400, 150, l8_1[0])


maxes = r4
arr_1 = l4_1
arr_2 = l4_2; arr_2_ax = r'$\sigma_{yx}$, МПа'
#arr_2 = l4_3; arr_2_ax = r'$\sigma_{xx}$, МПа'

rast = maxes[0]
min_y = maxes[1]
max_y = maxes[2]
min_z = maxes[3]


fig = plt.figure(figsize=(4, 4))

ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.set_box_aspect(aspect=(1, 1, 0.2))
ax.view_init(9, 190)

# Create the mesh in polar coordinates and compute corresponding Z.
r = np.linspace(0, rast, 60)
p = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 60)
R, P = np.meshgrid(r, p)
# Z = ((R**2 - 1)**2)

data_lin = np.array(arr_1)
Z = []
for _ in range(60):
    Z.append(data_lin)
Z = np.array(Z)

# Express the mesh in the cartesian system.
X, Y = R*np.cos(P), R*np.sin(P)


# Plot the surface.
ax.plot_surface(X, Y, Z, cmap=cm.viridis, linewidth=0.2, edgecolor='k')

# Tweak the limits and add latex math labels.
ax.set_zlim(min_z, 0)
ax.set_xlabel(r'$y$, мкм', labelpad=8)
ax.set_ylabel(r'$x$, мкм', labelpad=20)
ax.zaxis.set_rotate_label(False)  # disable automatic rotation
ax.set_zlabel(r'$h$, мкм', rotation=90)


# -----------------------------------------------
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.set_box_aspect(aspect=(1, 1, 0.2))
ax.view_init(9, 190)


data_lin2 = np.array(arr_2)
Q = []
for _ in range(60):
    Q.append(data_lin2)
Q = np.array(Q)

# Express the mesh in the cartesian system.
X2, Y2 = R*np.cos(P), R*np.sin(P)

# Plot the surface.
ax.plot_surface(X2, Y2, Q, cmap=cm.cividis, linewidth=0.2, edgecolor='k')

# Tweak the limits and add latex math labels.
ax.set_zlim(min_y, max_y)
ax.set_xlabel(r'$y$, мкм', labelpad=8)
ax.set_ylabel(r'$x$, мкм', labelpad=20)
ax.zaxis.set_rotate_label(False)  # disable automatic rotation
ax.set_zlabel(arr_2_ax, rotation=90)


fig.tight_layout()
plt.show()
