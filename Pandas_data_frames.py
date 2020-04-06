import numpy as np
import  pandas as pd

index = 'r1 r2 r3 r4 r5 r6 r7 r8 r9 r10'.split()
cols = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()

arr_2d = np.arange(1,101).reshape(10,10)
# print(arr_2d)

df = pd.DataFrame( data = arr_2d , index = index , columns = cols )
print("The data frame is given below:\n\n")
print(df)

print("--------------------------------------------------------------------")
print(df['c1'])

print("--------------------------------------------------------------------")
print(df[['c1','c3']])
print("--------------------------------------------------------------------")
print(df['c8']['r1'])
print("--------------------------------------------------------------------")
print("Adding new column to the data frame")
# df['tejas'] = df['r1'] + df ['r6'] # we cant  create a new column using columns
df['tejas'] = df['c1'] + df ['c6']
print(df)
print("Droping the column")
print(df.drop('tejas', axis = 1))
print(df.drop('r1'))
print(df)
# Drop dosen't permanently delete the values until you specify parameter inplace = True
print("-----------------------------------------------------------")
df.drop('tejas', axis = 1, inplace = True)
print(df)
# Delete a row permanently
# Defut axis will be 0 means rows
#df.drop('r1', inplace = True)
# print(df)
print("-----------------------------------------------------------")
print("Accessing data of rows")
#loc gives the values based on the keys
print("The elements of row 1 using loc are:\n",df.loc['r1'])
#iloc gives the values based on the index
print("The elements of row 1 using iloc are:\n",df.iloc[0])
print("The fourth column element of the 3 rd row is:",df.loc['r3','c4'])
# df.loc['r3','c4']   this should always be rows followed by columns
print("-----------------------------------------------------------")
print("The elements of 8th and 5th row are:")
print(df.loc[['r8','r5']])
print("-----------------------------------------------------------")
print("The subset of the data frame is:")
print(df.loc[['r2','r1'],['c3','c5']])
print("-----------------------------------------------------------")
print("Conditional selection")
print("The elements of data frame which are greater than 50 are")
print(df[df >25])
print("The elements of data frame divisible by 2 and 5 are")
cond = (df%2 == 0 ) & (df%3 == 0 )
print(df[cond])
# where ever the value is not present we will get NaN
# We usually do this operation on selective data frame
# Condition On a column
cond1  = (df['c1']%3) == 0
print("The elements of column 1 which are divisible by 3")
print(df[cond1])

print("If elements of column 1 are divisible by 3 , then show values of column 3 and column 7")
print(df[cond1][['c3','c7']])
# Try
# print("The elements of row 2 divivsble by 2")
# print(df[cond2]

print("The elements satisfying condition greater than 5 and show just 5 and 8 row")
print(df[df['c1']>5][['c1','c2','c3','c4','c5']].loc[['r5','r8']])

print("The elements satisfying multiple conditions")
print(df[(df['c1']>5)&(df['c2']%6 == 0)][['c3','c5']].loc['r2'])
print("-----------------------------------------------------------")

lst = 'a b c d e f g h i j'.split()
print(lst)
# @ Adding a new column which will act as index to the data frame
df['new_index'] = lst
print("The data frame after adding new index is")
print(df)


# Now the index will be changed from r1 ... to a ,b ..
df.set_index(keys = 'new_index', inplace = True)
print(df)
print("Accessing the data frame using new index values")
print(df.loc[['a','b']])
print("-----------------------------------------------------------------------")
# Head return the first n rows
print("The first 3 rows are")
print(df[df['c1'] > 25].head(3)[['c2','c3']])
print("-----------------------------------------------------------------------")
print("The summary of the data frame")
print(df.info())
print("The description of the data frame")
print(df.describe())
print("The mean value of clumn 1 is")
print(df['c1'].mean())
print("The mean value of row 1 is")
print(df.mean(axis = 1).loc['a'])
print(df.mean(axis = 1))