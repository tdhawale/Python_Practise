import numpy as np
import pandas as pd

# Hierarchical indexing makes it possible to have multiple (two or more) index levels on an axis.
# Somewhat abstractly, it provides a way to work with higher dimensional data in a lower dimensional form.
index = [['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,1,2]]
# print(index)
arr = np.random.randint(1,10, size = (1,10))[0]
print(arr)

# Creating a series
ser = pd.Series(data = arr , index = index )
print(ser)

print("The series with index a is :")
print(ser['a'])
print("The  2 element of this series is")
print(ser['a'][1])

cols = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()
arr2 = np.random.randint(1,100, size = (10,10))
# print(arr2)
df = pd.DataFrame(data = arr2 , index = index, columns = cols)
print(df)

print("---------------------------------------------------")
print("Accessing the row elements of a hierarchial data frame")
print(df.loc['a'] )
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# Idea is to go from outside to inside
print(df.loc['a'].loc[2]['c5'] )

print("---------------------------------------------------")
print("The index names for hierarchical data frame is:",df.index.names)
# Setting up indexes for Hierarchical data frame
df.index.names = ['L1', 'L2']       # Level 1 index and level 2 index
print("The index names for hierarchical data frame is:",df.index.names)
print("Now the data frame will look like:")
print(df.loc[: ,['c1','c2','c3']])
print("---------------------------------------------------")
print("Filtering based on the secondary index")
print(df)
# GEt data of a specified column
# print(df.xs('c3', axis = 1))
# FIltering all values where level 2 value is 1
# using .loc it would have been possible to filter
# index level 'L1'
print(df.xs(key = 1 , level = 'L2'))

# Here we have 2 level indexing . We can also have 3 level indexing.
# Please check df.xs() documentation

