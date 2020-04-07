import numpy as np
import  pandas as pd

print("The first data frame is")
df1 = pd.DataFrame({'key': ['a','b','c','d','e'], 'A1': range(5),'B1' : range(5,10)}, index =
					['i1','i2','i3','i4','i5'])
print(df1)
					# The first data frame is
					#    key  A1  B1
					# i1   a   0   5
					# i2   b   1   6
					# i3   c   2   7
					# i4   d   3   8
					# i5   e   4   9
print("--------------------------------------------------------------------------------------")
print("The second data frame is")
df2 = pd.DataFrame({'key': ['a','b','c'], 'A2': range(3),'B2' : range(3,6)}, index =
					['i1','i2','i3'])
print(df2)
					# The second data frame is
					#    key  A2  B2
					# i1   a   0   3
					# i2   b   1   4
					# i3   c   2   5


print("--------------------------------------------------------------------------------------")
print("Merging the data frame")
# how = inner , outer , left , right
# Inner Join = intersection on key specified
# Full outer join = all the elements of all data frames
# left outer join = all the elements of left data frame + common elements in right data frame
# right outer join = all the elements of right data frame + common elements in left data frame
print("The Inner Join of the data frames is")
print(pd.merge(df1, df2 , how = 'inner', on = 'key' ))
					# Merging the data frame
					#   key  A1  B1  A2  B2
					# 0   a   0   5   0   3
					# 1   b   1   6   1   4
					# 2   c   2   7   2   5

print("---------------------------------------------------------------------------")
print("The full outer join of the data frames is")
print(pd.merge(df1, df2 , how = 'outer', on = 'key' ))
					# The full outer join of the data frames is
					#   key  A1  B1   A2   B2
					# 0   a   0   5  0.0  3.0
					# 1   b   1   6  1.0  4.0
					# 2   c   2   7  2.0  5.0
					# 3   d   3   8  NaN  NaN
					# 4   e   4   9  NaN  NaN
print("---------------------------------------------------------------------------")
print("The left outer join of the data frames is")
print(pd.merge(df1, df2 , how = 'left', on = 'key' ))
					# The left outer join of the data frames is
					#   key  A1  B1   A2   B2
					# 0   a   0   5  0.0  3.0
					# 1   b   1   6  1.0  4.0
					# 2   c   2   7  2.0  5.0
					# 3   d   3   8  NaN  NaN
					# 4   e   4   9  NaN  NaN

print("---------------------------------------------------------------------------")
print("The right outer join of the data frames is")
print(pd.merge(df1, df2 , how = 'right', on = 'key' ))
					# The right outer join of the data frames is
					#   key  A1  B1  A2  B2
					# 0   a   0   5   0   3
					# 2   c   2   7   2   5
					# 1   b   1   6   1   4
print("---------------------------------------------------------------------------")
left = pd.DataFrame({'key1' : ['a' , 'a' , 'b' , 'c'] ,
                     'key2' : ['a' , 'b' , 'a' , 'b'] ,
                     'A' : ['A0' , 'A1' , 'A2' , 'A3'] ,
                     'B' : ['B0' , 'B1' , 'B2' , 'B3']})

right = pd.DataFrame({'key1' : ['a' , 'b' , 'b' , 'c'] ,
                      'key2' : ['a' , 'b' , 'a' , 'a'] ,
                      'C' : ['C0' , 'C1' , 'C2' , 'C3'] ,
                      'D' : ['D0' , 'D1' , 'D2' , 'D3']})
print(left)
					#   key1 key2   A   B
					# 0    a    a  A0  B0
					# 1    a    b  A1  B1
					# 2    b    a  A2  B2
					# 3    c    b  A3  B3
print("--------------------------------------------------------------------")
print(right)
					#   key1 key2   C   D
					# 0    a    a  C0  D0
					# 1    b    b  C1  D1
					# 2    b    a  C2  D2
					# 3    c    a  C3  D3
print("--------------------------------------------------------------------")
print("Merging based on multiple keys")
print(pd.merge(left, right , how = 'right', on = ['key1','key2'] ))
					#   key1 key2    A    B   C   D
					# 0    a    a   A0   B0  C0  D0
					# 1    b    a   A2   B2  C2  D2
					# 2    b    b  NaN  NaN  C1  D1
					# 3    c    a  NaN  NaN  C3  D3
					
					
print("--------------------------------------------------------------------")
print("CONCATENATION")
# Referred as binding. The dimensions should be same
del df1 , df2
print("The first data frame is")
df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']}, index = [0,1,2,3])
print(df1)
					# The first data frame is
					#     A   B   C   D
					# 0  A0  B0  C0  D0
					# 3  A3  B3  C3  D3
					# 1  A1  B1  C1  D1
					# 2  A2  B2  C2  D2
print("--------------------------------------------------------------------------")
print("The second data frame is")
df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                    'B':['B4','B5','B6','B7'],
                    'C':['C4','C5','C6','C7'],
                    'D':['D4','D5','D6','D7']}, index = [4,5,6,7])
print(df2)
					# The second data frame is
					#     A   B   C   D
					# 4  A4  B4  C4  D4
					# 5  A5  B5  C5  D5
					# 6  A6  B6  C6  D6
					# 7  A7  B7  C7  D7
print("---------------------------------------------------------------")
print(pd.concat([df1,df2], axis = 1))
# concatenate based on columns so since df2 dosent have column 0,1,2,3
# tha is why it is showing NaN
					#      A    B    C    D    A    B    C    D
					# 0   A0   B0   C0   D0  NaN  NaN  NaN  NaN
					# 1   A1   B1   C1   D1  NaN  NaN  NaN  NaN
					# 2   A2   B2   C2   D2  NaN  NaN  NaN  NaN
					# 3   A3   B3   C3   D3  NaN  NaN  NaN  NaN
					# 4  NaN  NaN  NaN  NaN   A4   B4   C4   D4
					# 5  NaN  NaN  NaN  NaN   A5   B5   C5   D5
					# 6  NaN  NaN  NaN  NaN   A6   B6   C6   D6
					# 7  NaN  NaN  NaN  NaN   A7   B7   C7   D7
print(pd.concat([df1,df2], ))
# concatenate based on rows # No NaN because rows A , B, C ,D  present in
# both data frames

					#     A   B   C   D
					# 0  A0  B0  C0  D0
					# 1  A1  B1  C1  D1
					# 2  A2  B2  C2  D2
					# 3  A3  B3  C3  D3
					# 4  A4  B4  C4  D4
					# 5  A5  B5  C5  D5
					# 6  A6  B6  C6  D6
					# 7  A7  B7  C7  D7




# pd.concat takes an Iterable as its argument. Hence, it cannot take DataFrames directly as its argument.
# Also Dimensions of the DataFrame should match along axis while concatenating.

# pd.concat works on both axes. while pd.merge works on columns
# pd.concat has inner(default) and outer joins only, while pd.merge left,right,outer,inner(default)

# pd.DataFrame.merge() has the option to set the column suffixes when merging columns with the same name
# while for pd.concat this is not possible.
print("---------------------------------------------------------------------------------------")
print("Group By")

# Groupby is one of the most important and key functionality in pandas. It allows us to group data together, call
# aggregate functions and combine the results in three steps split-apply-combine:
#
#
# Split: In this process, data contained in a pandas object (e.g. Series, DataFrame) is split into groups based
# on one or more keys that we provide. The splitting is performed on a particular axis of an object.
# For example, a DataFrame can be grouped on its rows (axis=0) or its columns (axis=1).
#
# apply: Once splitting is done, a function is applied to all groups independently, producing a new value.
#
# combine: Finally, the results of all those functions applications are combined into a resultant object.
# The form of the resulting object will usually depend on what's being done to the data.

# Create a dataframe
data = {'Store':['Walmart','Walmart','Costco','Costco','Target','Target'],
       'Customer':['Tim','Jermy','Mark','Denice','Ray','Sam'],
       'Sales':[150,200,550,90,430,120],
        'Salary':[1000,1200,1000,1400,1200,1300]}
df = pd.DataFrame(data)
print(df)

print("---------------------------------------------")
print("Group by Customer")
by_customer = df.groupby('Customer')
# The aggregation function will consider only the numeric values
print(by_customer.mean().loc[['Mark','Ray','Sam']])

print("---------------------------------------------")
print("Group by Store")
by_store = df.groupby('Store')
# The aggregation function will consider only the numeric values
print(by_store.sum())
# You can do all the aggregation function on the grouped data frame