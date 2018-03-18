"""
status:: Accepted
this is highly recommended for sympy
Cursor

"""
from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111,facecolor='#FFFFCC')

x,y = 4*(np.random.rand(2,100)- .5)
ax.plot(x,y,'o')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)

cursor = Cursor(ax,useblit=True,color='red',linewidth=2)
plt.show()