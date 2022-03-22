# -*- coding: utf-8 -*-
"""
Draw artistic graphs, matematically similar but graphically quite different.

@author: imbroscb
"""

import numpy as np
import matplotlib.pyplot as plt

# %% graph 1

# define variables
t = np.linspace(0, 10 * np.pi, 12000)
arg1 = np.exp(np.cos(t))
arg2 = 3 * np.cos(4 * t)
arg3 = (np.sin(t/45))**5
x = np.sin(t) * (arg1 + arg2 - arg3)
y = np.cos(t) * (arg1 - arg2 - arg3)

# plot
plt.figure()
plt.plot(x, y, c='black')
plt.axis('off')

# %% graph 2

# define variables
t = np.linspace(0, 10 * np.pi, 12000)
arg1 = np.exp(np.cos(t))
arg2 = 3 * np.cos(4 * t)
arg3 = (np.sin(t/45))**5
x = np.sin(t) * (arg1 + arg2 - arg3)
y = np.cos(t) * (-arg1 - arg2 - arg3)

# plot
plt.figure()
plt.plot(x, y, c='black')
plt.axis('off')

# %% graph 3

# define variables
t = np.linspace(0, 20 * np.pi, 12000)
arg1 = np.exp(np.cos(t))
arg2 = 3 * np.cos(4 * t)
arg3 = (np.sin(t/90))**5
x = np.sin(t) * (arg1 - arg2 - arg3)
y = np.cos(t) * (-arg1 - arg2 - arg3)

# plot
plt.figure()
plt.plot(x, y, c='black')
plt.axis('off')

