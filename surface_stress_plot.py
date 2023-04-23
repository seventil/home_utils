from mpl_toolkits import mplot3d
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from scipy import interpolate

"""
Created on Wed May 26 10:53:05 2021

@author: User
"""

font = {'family': 'serif',
        'size': 16}

matplotlib.rc('font', **font)


def data1():
    data1 = [
        [-60, 85, -160, 130, -82, 63, -40],
        [-30, 115, -192, 147, -102, 37, 30],
        [15, 67, -83, 101, -93, 11, -5]
    ]
    return data1


def data2():
    data2 = [
        [-13, 130, -110, 150, -70, 50, 8],
        [-37, 122, -97, 180, -70, 50, -11],
        [-22, 79, -60, 171, -60, 40, -15]
    ]
    return data2


def interp_surface(data):
    times_to_enlarge_rows = 4
    times_to_enlarge_cols = 4

    for index, row in enumerate(data):
        x = np.linspace(0, len(row)-1, len(row))
        f = interpolate.interp1d(x, row, kind="quadratic")
        x_new = np.linspace(0, len(row)-1, len(row)*times_to_enlarge_rows)
        data[index] = f(x_new)

    tr_surface = list(np.transpose(data))

    for index, row in enumerate(tr_surface):
        x = np.linspace(0, len(row)-1, len(row))
        f = interpolate.interp1d(x, row, kind="quadratic")
        x_new = np.linspace(0, len(row)-1, len(row)*times_to_enlarge_cols)
        tr_surface[index] = f(x_new)

    return np.array(tr_surface)
    # return np.array(randfunc(func))


def cmaps(data):
    cmap_min = data[0][0]
    cmap_max = data[0][0]
    
    for row in data:
        if cmap_min > min(row):
            cmap_min = min(row)
        if cmap_max < max(row):
            cmap_max = max(row)
    
    return cmap_min, cmap_max

# def surface2():
#     func = [218, 167, 122, 69, 37,
#             32, 25, 23, 53, 245]
#     return np.array(randfunc(func))

# def surface3():
#     func = [221, 0, -300, -340, -450, 
#             -460, -400, -460, -400, 23]
#     func = [item * 1.5 for item in func]
#     return np.array(randfunc(func))

# def randfunc(func):
#     output2d = []
#     for _ in range(10):
#         output = []
#         rng = np.random.default_rng()
#         for point in func:
#             newval = point + 400*(rng.random()-0.5)*0.33
#             output.append(newval)
#         output2d.append(output)

#     return output2d


# Axes arrays
# Z1 = interp_surface(data1())
# Z1_orig = np.transpose(np.array(data1()))

# x = np.linspace(2, len(Z1_orig[0])*2, len(Z1[0]))
# y = np.linspace(2, len(Z1_orig)*2, len(Z1))
# X, Y = np.meshgrid(x, y)

# x_orig = np.linspace(2, len(Z1_orig[0])*2, len(Z1_orig[0]))
# y_orig = np.linspace(2, len(Z1_orig)*2, len(Z1_orig))
# X_orig, Y_orig = np.meshgrid(x_orig, y_orig)

Z2 = interp_surface(data2())
Z2_orig = np.transpose(np.array(data2()))

x2 = np.linspace(2, len(Z2_orig[0])*2, len(Z2[0]))
y2 = np.linspace(2, len(Z2_orig)*2, len(Z2))
X2, Y2 = np.meshgrid(x2, y2)

x_orig2 = np.linspace(2, len(Z2_orig[0])*2, len(Z2_orig[0]))
y_orig2 = np.linspace(2, len(Z2_orig)*2, len(Z2_orig))
X_orig2, Y_orig2 = np.meshgrid(x_orig2, y_orig2)


# Plots

fig = plt.figure()
ax = plt.axes(projection='3d')

cmap_min, cmap_max = cmaps(data1())

# surf1 = ax.plot_surface(X, Y, Z1, vmin=cmap_min, vmax=cmap_max,
#                         alpha=0.6, cmap='summer', edgecolor='black',
#                         linewidth=0.2)
# points = ax.scatter(X_orig, Y_orig, Z1_orig, s=20, c='black')
# fig.colorbar(surf1, shrink=0.5)

surf2 = ax.plot_surface(X2, Y2, Z2, vmin=cmap_min, vmax=cmap_max,
                        alpha=0.6, cmap='autumn', edgecolor='black',
                        linewidth=0.2)
points = ax.scatter(X_orig2, Y_orig2, Z2_orig, s=20, c='black')
fig.colorbar(surf2, shrink=0.5)


plt.xticks(np.arange(2, 7, 1))
plt.yticks(np.arange(2, 15, 2))

ax.set_xlabel('x, мм', labelpad=12)
ax.set_ylabel('y, мм', labelpad=12)
ax.zaxis.set_rotate_label(False)
# ax.set_zlabel('Осевые напряжения, МПа', labelpad=16, rotation=90)
ax.set_zlabel('Окружные напряжения, МПа', labelpad=16, rotation=90)

# ax.text(3, 0, -700, "h = 0 мкм")
# ax.text(13, 0, -90, "h = 10 мкм")
# ax.text(0, 20, 350, "h = 100 мкм")

plt.show()

