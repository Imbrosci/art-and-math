# -*- coding: utf-8 -*-
"""
Draw a graph resembling a butterfly.

@author: imbroscb
"""

import numpy as np
import matplotlib.pyplot as plt

# %%


# body
t = np.linspace(0, 10 * np.pi, 12000)
arg1 = np.exp(np.cos(t))
arg2 = 2 * np.cos(4 * t)
arg3 = (np.sin(t/45))**5
x = np.sin(t) * (arg1 - arg2 - arg3)
y = np.cos(t) * (arg1 - arg2 - arg3)

# antennae
x2_1 = np.linspace(0.1, 0.6, 1000)
x2_2 = np.linspace(-0.1, -0.6, 1000)
y2 = 2.5 * np.sin(x2_1)**0.5 + 0.8
t = np.linspace(0, 3 * np.pi, 1000)
x3_1 = 0.1 * np.cos(t) + 0.65
x3_2 = 0.1 * np.cos(t) - 0.65
y3 = 0.1 * np.sin(t) + 2.76

# plot
plt.figure()
plt.plot(x, y, c='black')
plt.plot(x2_1, y2, linewidth=2, c='black')
plt.plot(x2_2, y2, linewidth=2, c='black')
plt.plot(x3_1, y3, linewidth=2, c='black')
plt.plot(x3_2, y3, linewidth=2, c='black')
plt.axis('off')


