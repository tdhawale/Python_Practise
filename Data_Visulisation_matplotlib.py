# https://matplotlib.org/gallery/index.html
# https://matplotlib.org/tutorials/introductory/images.html#sphx-glr-tutorials-introductory-images-py

import matplotlib.pyplot as plt
import  numpy as np
import  math as m
# plt.show()

x = np.arange(11)
y = list(map(lambda num: int(m.pow(num,2)),x))
#print(x)
					# [ 0  1  2  3  4  5  6  7  8  9 10]
#print(y)
					# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#------------------------------------------------------------------------------------------------------------
# Plotting a  single figure directly
#------------------------------------------------------------------------------------------------------------
plt.figure(1)
plt.bar(x,y , color = 'red')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Simple Plotting example')





#------------------------------------------------------------------------------------------------------------
# SubPlot by specifying the subplot location
#------------------------------------------------------------------------------------------------------------

plt.figure(2)
# plt.subplot(2,2,1) subpplot will be of size 2 rows 2 columns . 1 represent the figure number i.e
#                                                                1st row 1st column
plt.subplot(2,2,1)
plt.bar(x,y, color = 'red')

# subplot 2x2 , figure number 2 means 2nd row 1st column
ax =plt.subplot(2,2,2)
labels = ["X", "Y"]
ax.stackplot(x, y, labels=labels)
ax.legend(loc='upper left')

# subplot 2x2 , figure number 3 means 1st row 2nd column
plt.subplot(2,2,3)
plt.stem(x, y, use_line_collection=True)

# subplot 2x2 , figure number 3 means 2nd row 2nd column
plt.subplot(2,2,4)
plt.plot(x*0.1, y, 'o-', color='purple', label='No mask')
# plt.broken_barh(x,y, color = 'yellow')




#------------------------------------------------------------------------------------------------------------
# Plot a single figure specifying axis
#------------------------------------------------------------------------------------------------------------
fig3 = plt.figure()
ax = fig3.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Title')





#------------------------------------------------------------------------------------------------------------
# Plot a single figure and an inset(another graph inside it) inside it
#------------------------------------------------------------------------------------------------------------
fig4 = plt.figure()
ax_main = fig4.add_axes([0.1,0.1,0.8,0.8])
ax_inset = fig4.add_axes([0.2,0.5,0.3,0.3])
# ax_inset = fig4.add_axes([X axis point,Y axis point,length,breadth])
ax_main.plot(x,y,'b')
ax_main.set_xlabel('X')
ax_main.set_ylabel('Y')
ax_main.set_title('Plotting X against Y')

ax_inset.plot(y,x, 'r')
ax_inset.set_xlabel('X')
ax_inset.set_ylabel('Y')
ax_inset.set_title('Plotting Y against X')






#------------------------------------------------------------------------------------------------------------
# SubPlot by specifying axis
#------------------------------------------------------------------------------------------------------------
# Colour styles https://matplotlib.org/3.1.0/gallery/color/named_colors.html
					# blue - b
					# green - g
					# red - r
					# magenta - m
					# cyan - c
					# yellow -w
					# black - k
					# white - w
					# Many different colours are there

# Line Styles https://matplotlib.org/2.0.2/api/lines_api.html
					# '-' or 'solid'	solid line
					# '--' or 'dashed'	dashed line
					# '-.' or 'dashdot'	dash-dotted line
					# ':' or 'dotted'	dotted line
					# 'None'	draw nothing
					# ' '	draw nothing
					# ''	draw nothing
					
# Line Marker
					# '.' point  marker
					# ',' pixel  marker
					# 'o' circle marker
					# 'v' triangle_down marker
					# '^' triangle_up marker
					# '<' triangle_left marker
					# '>' triangle_right marker
					# '1' tri_down marker
					# '2' tri_up marker
					# '3' tri_left marker
					# '4' tri_right marker
					# 's' square marker
					# 'p' pentagon marker
					# '*' star marker
					# 'h' hexagon1 marker
					# 'H' hexagon2 marker
					# '+' plus marker
					# 'x' x marker
					# 'D' diamond marker
					# 'd' thin_diamond marker
					# '|' vline marker
					# '_' hline marker
# fig , axes = plt.subplots( nrows= 2 , ncols=2, sharex = True, sharey = True)
fig5 ,axes5 = plt.subplots(nrows = 2 , ncols = 2) # figure will have two columns and 1 row
axes5[0][0].plot(x,y,'cv--')
axes5[0][0].set_xlabel('X')
axes5[0][0].set_ylabel('Y')
axes5[0][0].set_title('Plotting X against Y')



axes5[0][1].plot(x,y,'mD:')
axes5[0][1].set_xlabel('X')
axes5[0][1].set_ylabel('Y')
axes5[0][1].set_title('Plotting X against Y')



axes5[1][0].plot(x,y,'rH-')
axes5[1][0].set_xlabel('X')
axes5[1][0].set_ylabel('Y')
axes5[1][0].set_title('Plotting X against Y')



# plt.plot() # You can different option which you can explore in plt.plot(ctrl+q)
axes5[1][1].plot(x,y, color = 'olive' , alpha = 0.8 , linestyle  = ':' , marker = 'o' , markersize = 4,
                 markerfacecolor = 'black')
axes5[1][1].set_xlabel('X')
axes5[1][1].set_ylabel('Y')
axes5[1][1].set_title('Plotting X against Y')
fig5.tight_layout()






#------------------------------------------------------------------------------------------------------------
# Aspect Ratio
#------------------------------------------------------------------------------------------------------------
fig6 = plt.figure(figsize= (10,5), dpi=100)
ax6 = fig6.add_axes([0.1,0.1,0.8,0.8])
ax6.plot(x,y , 'r*--' , label = 'freq is 10Hz')
ax6.plot(y,x , 'y*--' , label = 'freq is 20Hz')
ax6.set_xlabel('X')
ax6.set_ylabel('Y')
ax6.set_title('Multiple plots on same graph')
# ax6.legend(loc = 4)         # lower right corner
# ax6.legend(loc = 3)         # lower left corner
# ax6.legend(loc = 2)         # upper left corner
ax6.legend(loc = 1)           # upper right corner
# ax6.legend(loc = 0)         # Matplot lib decides the location of the legend





#------------------------------------------------------------------------------------------------------------
# Set axis limits
#------------------------------------------------------------------------------------------------------------
fig7 ,axes7 = plt.subplots(nrows = 1, ncols = 3,figsize= (10,5)) # figure will have two rows and two column
# It is a 1D array
axes7[0].plot(x,y, 'ro--')
axes7[0].set_title('Default')


axes7[1].plot(x,y , 'bx:')
axes7[1].axis('tight')
axes7[1].set_title('tight')


axes7[2].plot(x,y, 'mD-')
axes7[2].set_title('Custom')
axes7[2].set_xlim([0,4])
axes7[2].set_ylim([0,50])


# Matplotlib gives us the option to save the figure in defferent formats
# It will save the fig in the directory
# fig7.savefig('fig7.png',dpi = 100)


#------------------------------------------------------------------------------------------------------------
# Scatter Plot
#------------------------------------------------------------------------------------------------------------
plt.figure(8)
plt.scatter(x,y)




#------------------------------------------------------------------------------------------------------------
# Histogram
#------------------------------------------------------------------------------------------------------------
plt.figure(9)
# arr = np.array(np.random.randint(1,100, size = (1,100)))
# plt.hist(arr)

from random import sample
data = sample(range(1, 1000), 100)
plt.hist(data)




#------------------------------------------------------------------------------------------------------------
# Box Plot
#------------------------------------------------------------------------------------------------------------
plt.figure(10)
# boxplot
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# rectangular box plot
plt.boxplot(data,vert=True,patch_artist=True);
# plt.boxplot(arr4)
















#
plt.show()
plt.tight_layout()