# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 17:24:08 2018

@author: srini
"""

import matplotlib.pyplot as plt
import numpy.random as rnd
from matplotlib.patches import Ellipse

#NUM = 250

ells = Ellipse(xy=[1,1], width=10, height=5, angle=0,ec='b',fc='none')

fig = plt.gcf()
ax = fig.gca()
ax.add_artist(ells)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

plt.show()