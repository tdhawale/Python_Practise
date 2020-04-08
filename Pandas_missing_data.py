import numpy as np
import  pandas as pd

data_dic =  {'A':[1,2,np.nan,4,np.nan],
            'B':[np.nan,np.nan,np.nan,np.nan,np.nan],
            'C':[11,12,13,14,15],
            'D':[16,np.nan,18,19,20]}
df = pd.DataFrame(data_dic)
print(df)
                    #      A   B   C     D
                    # 0  1.0 NaN  11  16.0
                    # 1  2.0 NaN  12   NaN
                    # 2  NaN NaN  13  18.0
                    # 3  4.0 NaN  14  19.0
                    # 4  NaN NaN  15  20.0

# You can also create a missing data data frame using the folloting method
# index = 'r1 r2'.split()
# cols = 'c1 c2'.split()
#
# arr_2d = [['1',np.nan],['1','2']]
# # print(arr_2d)
#
# df = pd.DataFrame( data = arr_2d , index = index , columns = cols )
# print(df)
print("Print the values which are null")
print(df.isnull())

# Pandas is ignoring NaN values in calculation.
# So Pandas is used to handle the missing data in python
print("-------------------------------------------------------")
print("The sum of column A is ",df['A'].sum())
print("The mean of all the elements of row 1 is: ",df.mean(axis = 1).loc[1])

# All rows which have 3 non NaN elements will be returned
print(df.dropna(thresh = 3))
                    #      A   B   C     D
                    # 0  1.0 NaN  11  16.0
                    # 3  4.0 NaN  14  19.0
# Dropna value is performed on rows . We can also perform it on columns
print("-------------------------------------------------------------")
print(df.dropna(axis = 1, thresh = 5))
                    #     C
                    # 0  11
                    # 1  12
                    # 2  13
                    # 3  14
                    # 4  15
print("-------------------------------------------------------------")
print(df)
df1 = df.copy()
print(df1)
                    #      A   B   C     D
                    # 0  1.0 NaN  11  16.0
                    # 1  2.0 NaN  12   NaN
                    # 2  NaN NaN  13  18.0
                    # 3  4.0 NaN  14  19.0
                    # 4  NaN NaN  15  20.0
#You can also drop columns . Inplace is use to keep the changes permanentely
df1.drop(['C','D'], axis = 1, inplace = True)
print(df1)
                    #      A   B
                    # 0  1.0 NaN
                    # 1  2.0 NaN
                    # 2  NaN NaN
                    # 3  4.0 NaN
                    # 4  NaN NaN
print("------------------------------------------------------------------")
del df1
df1 = df.copy()
df1.fillna(value = 111, inplace = True)
print(df1)
                    #        A      B   C      D
                    # 0    1.0  111.0  11   16.0
                    # 1    2.0  111.0  12  111.0
                    # 2  111.0  111.0  13   18.0
                    # 3    4.0  111.0  14   19.0
                    # 4  111.0  111.0  15   20.0
print("------------------------------------------------------------------")
del df1
df1 = df.copy()
df1.fillna(value = (df.mean(axis = 1).loc[1]), inplace = True)
print(df1)
print("------------------------------------------------------------------")
# Method Forward fill . wherever there is NaN , the previous value will be forwarded
# to the NaN cell
# Since there is no value for column B , nothing can be filled
del df1
df1 = df.copy()
df1.fillna(method = 'ffill', inplace = True)
print(df1)
                    # Original before forward fill 2 will go to NaN , 4 will go to Nan
                    # since for column B there is no value to be forwarded it will remain NaN
                    #      A   B   C     D
                    # 0  1.0 NaN  11  16.0
                    # 1  2.0 NaN  12   NaN
                    # 2  NaN NaN  13  18.0
                    # 3  4.0 NaN  14  19.0
                    # 4  NaN NaN  15  20.0




                    #      A   B   C     D
                    # 0  1.0 NaN  11  16.0
                    # 1  2.0 NaN  12  16.0
                    # 2  2.0 NaN  13  18.0
                    # 3  4.0 NaN  14  19.0
                    # 4  4.0 NaN  15  20.0
print("------------------------------------------------------------------")
# Method Backward fill . wherever there is NaN , the next value will be forwarded
# to the NaN cell
del df1
df1 = df.copy()
df1.fillna(method = 'bfill', inplace = True)
print(df1)
                    # Original data frame.  4 will be in column A and index 2
                    # Since there is nothing in front of column A index 4 it will remain NaN
                    #      A   B   C     D
                    # 0  1.0 NaN  11  16.0
                    # 1  2.0 NaN  12   NaN
                    # 2  NaN NaN  13  18.0
                    # 3  4.0 NaN  14  19.0
                    # 4  NaN NaN  15  20.0
                    
                    
                    
                    
                    
                    #      A   B   C     D
                    # # 0  1.0 NaN  11  16.0
                    # # 1  2.0 NaN  12  18.0
                    # # 2  4.0 NaN  13  18.0
                    # # 3  4.0 NaN  14  19.0
                    # # 4  NaN NaN  15  20.0



