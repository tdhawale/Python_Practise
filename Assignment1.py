#######################################################################
# Author : Tejas Ravindra Dhawale
# Student Id : 6882910
#######################################################################
# References used :
#https://stackoverflow.com/questions/25505674/python-matplotlib-add-colorbar
#https://stackoverflow.com/questions/8931268/using-colormaps-to-set-color-of-line-in-matplotlib
#https://pythonforundergradengineers.com/quiver-plot-with-matplotlib-and-jupyter-notebooks.html
#https://problemsolvingwithpython.com/06-Plotting-with-Matplotlib/06.15-Quiver-and-Stream-Plots/
#######################################################################
# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib as mpl

# Reading the data set
data = pd.read_csv('field2.irreg.txt', sep=" " , header=None , skiprows= 6)


# Normalize and set color
cmap = plt.cm.coolwarm
cNorm  = colors.Normalize(vmin=0, vmax=1)
scalarMap = cmx.ScalarMappable(norm=cNorm,cmap=cmap)


# Calculating length of the arrow to determine the color values
length = np.hypot(data[3] , data[4])


# Plot Figure
fig = plt.figure()
ax  = fig.add_axes([0.1, 0.1, 0.7, 0.85])
ax.quiver(data[0],data[1],data[3],data[4],color = scalarMap.to_rgba(length) ,pivot='mid' , scale = 8  )
ax.set_title('Flow Visualization')
ax.set_aspect('equal')
ax.set_xlabel('X value of vector')
ax.set_ylabel('Y value of vector')
ax.use_sticky_edges = False


# Setting the Color Bar and it labels
cax = fig.add_axes([0.80, 0.10, 0.02, 0.85])
cb = mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=cNorm)
cax.set_yticklabels(['Low', '','', '', '','High'])
cb.set_label('Velocity of the particle')

# Save the plot as .png image
fig.savefig('Assignment1.png' , bbox_inches="tight" , dpi=150)
plt.show()