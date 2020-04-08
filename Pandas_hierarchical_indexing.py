import numpy as np
import pandas as pd

# Hierarchical indexing makes it possible to have multiple (two or more) index levels on an axis.
# Somewhat abstractly, it provides a way to work with higher dimensional data in a lower dimensional form.
index = [['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,1,2]]
# print(index)
arr = np.random.randint(1,10, size = (1,10))[0]
# print(arr)

# Creating a series
ser = pd.Series(data = arr , index = index )
print(ser)
					# a  1    3
					#    2    1
					#    3    8
					# b  1    4
					#    2    6
					#    3    1
					# c  1    7
					#    2    7
					# d  1    1
					#    2    9
					# dtype: int32

print("The series with index a is :")
print(ser['a'])
print("The  2 element of this series is")
print(ser['a'][1])

cols = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()
arr2 = np.random.randint(1,100, size = (10,10))
# print(arr2)
df = pd.DataFrame(data = arr2 , index = index, columns = cols)
print(df)
					#      c1  c2  c3  c4  c5  c6  c7  c8  c9  c10
					# a 1   9  68  88  74   6  88  47  90  74   63
					#   2  58  87  76  50  51  80  74  71  20   81
					#   3  34  32   5  11  65  35  31  36  65   68
					# b 1  62  80  57  16  57  27  77  45  18   41
					#   2  27  95  56  95  35  36  48  86  76   18
					#   3  97  57  46  50   7  49   4  21  27   41
					# c 1  58  85   7   4  63  85  70  57  93   84
					#   2  70  93  48  82  89  15  31  71  77   13
					# d 1  38  15  96  64  37  70   6  38  20   46
					#   2  81  31  56  97  62  44  37  65  84   81
print("---------------------------------------------------")
print("Accessing the row elements of a hierarchial data frame")
print(df.loc['a'] )
					# Accessing the row elements of a hierarchial data frame
					#    c1  c2  c3  c4  c5  c6  c7  c8  c9  c10
					# 1   9  68  88  74   6  88  47  90  74   63
					# 2  58  87  76  50  51  80  74  71  20   81
					# 3  34  32   5  11  65  35  31  36  65   68
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# Idea is to go from outside to inside
print(df.loc['a'].loc[2]['c5'] )

print("---------------------------------------------------")
print("The index names for hierarchical data frame is:",df.index.names)
					# The index names for hierarchical data frame is: [None, None]
# Setting up indexes for Hierarchical data frame
df.index.names = ['L1', 'L2']       # Level 1 index and level 2 index
print("The index names for hierarchical data frame is:",df.index.names)
					# The index names for hierarchical data frame is: ['L1','L2']
print("Now the data frame will look like:")
print(df.loc[: ,['c1','c2','c3']])
					#        c1  c2  c3
					# L1 L2
					# a  1    9  68  88
					#    2   58  87  76
					#    3   34  32   5
					# b  1   62  80  57
					#    2   27  95  56
					#    3   97  57  46
					# c  1   58  85   7
					#    2   70  93  48
					# d  1   38  15  96
					#    2   81  31  56
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

