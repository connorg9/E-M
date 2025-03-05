
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

a = 5
b = 2
N = 100

x = np.linspace(0, a, N)
y = np.linspace(0, b, N)
xx, yy = np.meshgrid(x, y)
V = np.zeros((N, N))

for i in range(N):
    V[0, i] = np.sin((2*np.pi*x[i])/a)
    V[i, 0] = 0
    V[N-1, i] = np.cos((2*np.pi*x[i])/a)
    V[i, N-1] = 0

for i in range(1, N-1):
    for j in range(1, N-1):
        V[i, j] = 1/4 * (V[i-1, j] + V[i+1, j] + V[i, j-1] + V[i, j+1])

V2 = V.copy()
max_error = 100
counter = 0
tol = 1e-4

while max_error > tol:
    new_V = V2.copy()
    for i in range(1, N-1):
        for j in range(1, N-1):
            new_V[i, j] = 1/4 * (V2[i-1, j] + V2[i+1, j] + V2[i, j-1] + V2[i, j+1])
    max_error = np.max(np.abs(new_V - V2))
    V2 = new_V.copy()
    counter += 1

fig = plt.figure(figsize = (8,8))
ax = plt.subplot(211)
ax.contourf(x, y, V2, cmap = cm.plasma)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect("equal", "datalim")

ax2 = plt.subplot(212, projection = "3d")
ax2.plot_surface(xx, yy, V2, cmap = cm.plasma)
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("V")
ax2.set_aspect("equal", "datalim")

plt.show()