import seaborn as sns
import matplotlib.pyplot as plt
# sns.get_dataset_names()    # Gives the data sets available in seaborn library

tips = sns.load_dataset('tips')
print(tips.head())
					#    total_bill   tip     sex smoker  day    time  size
					# 0       16.99  1.01  Female     No  Sun  Dinner     2
					# 1       10.34  1.66    Male     No  Sun  Dinner     3
					# 2       21.01  3.50    Male     No  Sun  Dinner     3
					# 3       23.68  3.31    Male     No  Sun  Dinner     2
					# 4       24.59  3.61  Female     No  Sun  Dinner     4
# tips1 = tips.copy()
#
# tips1.drop(['sex' , 'smoker' , 'day' , 'time'], axis = 1, inplace = True)
# print(tips1.head())
#
# plt.figure(1)
# sns.distplot(tips1)
#
# plt.figure(2)
sns.distplot(tips['total_bill'],kde = False, bins = 50)
plt.title('Figure 1')
# # Seaborn gives the ability to plot two variables in the data
# plt.figure(3)
sns.jointplot(x ='total_bill' , y ='tip' , data = tips)
plt.title('Figure 2')
#
# # Displaying the data in hexagon . Darker the color of the hexagon , more the data points
# plt.figure(4)
sns.jointplot(x ='total_bill' , y ='tip' , data = tips ,kind = 'hex')
plt.title('Figure 3')
#
# # Darker region shows where most of the data match up
# plt.figure(5)
sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')
plt.title('Figure 4')
# # Pair Plot
# plt.figure(6)


# plt.figure(8)
# sns.rugplot(tips['tip'])
fig , axs = plt.subplots()
sns.distplot(tips['total_bill']  ,kde = False)
# sns.rugplot(tips['total_bill'] , ax = axs[1] )
sns.kdeplot(tips['total_bill']  )
plt.title('Figure 5')

# sns.distplot(tips['total_bill'], kde = False)

# sns.pairplot(tips , hue = 'sex')
# plt.title('Figure 5')






























plt.show()

