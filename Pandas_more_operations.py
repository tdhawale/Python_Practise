import numpy as np
import pandas as pd
import  math as m

df = pd.DataFrame({'col_1':[1,2,3,4,5],
                   'col_2':[111,222,333,111,555],
                   'col_3':['alpha','bravo','charlie',np.nan,np.nan]}, index = [1,2,3,4,5])
print(df)
                    #    col_1  col_2    col_3
                    # 1      1    111    alpha
                    # 2      2    222    bravo
                    # 3      3    333  charlie
                    # 4      4    111      NaN
                    # 5      5    555      NaN
print("-----------------------------------------------------------------------------")
print("The info about the data frame is")
print(df.info())
                    # The info about the data frame is
                    # <class 'pandas.core.frame.DataFrame'>
                    # Int64Index: 5 entries, 1 to 5
                    # Data columns (total 3 columns):
                    #  #   Column  Non-Null Count  Dtype
                    # ---  ------  --------------  -----
                    #  0   col_1   5 non-null      int64
                    #  1   col_2   5 non-null      int64
                    #  2   col_3   3 non-null      object
                    # dtypes: int64(2), object(1)
                    # memory usage: 140.0+ bytes
                    # None
print("-----------------------------------------------------------------------------")
print("The first two rows of the data frame is")
print(df.head(2))
                    # The first two rows of the data frame is
                    #    col_1  col_2  col_3
                    # 1      1    111  alpha
                    # 2      2    222  bravo
print("-----------------------------------------------------------------------------")
print("The is null check is")
print(df.isnull())
                    # The is null check is
                    #    col_1  col_2  col_3
                    # 1  False  False  False
                    # 2  False  False  False
                    # 3  False  False  False
                    # 4  False  False   True
                    # 5  False  False   True
print("------------------------------ -----------------------------------------------")
print("The drop na(Handling missing data)")
print(df)
                    #    col_1  col_2    col_3
                    # 1      1    111    alpha
                    # 2      2    222    bravo
                    # 3      3    333  charlie
                    # 4      4    111      NaN
                    # 5      5    555      NaN
print()
print()
print(df.dropna()) # Default axis is 0 so it is dropping all the columns
# who has NaN
                    #    col_1  col_2    col_3
                    # 1      1    111    alpha
                    # 2      2    222    bravo
                    # 3      3    333  charlie
print()
print(df.dropna(axis = 1)) # axis = 1 for columns . It is droping all the
# columns which has NaN
                    #    col_1  col_2
                    # 1      1    111
                    # 2      2    222
                    # 3      3    333
                    # 4      4    111
                    # 5      5    555
print("-----------------------------------------------------------------------------")
print("Filling missing data")
print(df.fillna(value = 111))   # Note : inplace is not true
                    #    col_1  col_2    col_3
                    # 1      1    111    alpha
                    # 2      2    222    bravo
                    # 3      3    333  charlie
                    # 4      4    111      111
                    # 5      5    555      111
print(df.fillna(method = 'ffill'))
                    #    col_1  col_2    col_3
                    # 1      1    111    alpha
                    # 2      2    222    bravo
                    # 3      3    333  charlie
                    # 4      4    111  charlie
                    # 5      5    555  charlie
print("-----------------------------------------------------------------------------")
print("How many unique values are there in the column")
print(df['col_2'].unique())
                    # [111 222 333 555]
print("The number of unique elements in the data frame",df['col_2'].nunique() )
                    # The number of unique elements in the data frame 4
print("-----------------------------------------------------------------------------")
print("To show huw much times the value appears in the column")
print(df['col_2'].value_counts())
                    # 111    2
                    # 222    1
                    # 333    1
                    # 555    1
                    # Name: col_2, dtype: int64
print("-----------------------------------------------------------------------------")
print("Sort Values")
print(df.sort_values(by = 'col_2', ascending = False, na_position = 'first'))
                    #    col_1  col_2    col_3
                    # 5      5    555      NaN
                    # 3      3    333  charlie
                    # 2      2    222    bravo
                    # 1      1    111    alpha
                    # 4      4    111      NaN
print(df.sort_values(by = 'col_3', ascending = False, na_position = 'first'))
                    #    col_1  col_2    col_3
                    # 4      4    111      NaN
                    # 5      5    555      NaN
                    # 3      3    333  charlie
                    # 2      2    222    bravo
                    # 1      1    111    alpha
print("-----------------------------------------------------------------------------")
print("Conditional selection")
print(df)
                    #    col_1  col_2    col_3
                    # 1      1    111    alpha
                    # 2      2    222    bravo
                    # 3      3    333  charlie
                    # 4      4    111      NaN
                    # 5      5    555      NaN
print()
print()
print("Condition 1")
print(df[df['col_2']/111 > 2])
                    # Condition 1
                    #    col_1  col_2    col_3
                    # 3      3    333  charlie
                    # 5      5    555      NaN
print()
print()
print("Condition 2")
cond = (df['col_2']/111 > 2) & (df['col_3'] == 'charlie')
print(df[cond])
                    # Condition 2
                    #    col_1  col_2    col_3
                    # 3      3    333  charlie

print(df[cond].transpose())
                    #             3
                    # col_1        3
                    # col_2      333
                    # col_3  charlie
# print(df[(df['col_2']/111 > 2)])
print()
print()
print("Condition 3")
print(df[df['col_2']/111 > 2].loc[5])
                    # Condition 3
                    # col_1      5
                    # col_2    555
                    # col_3    NaN
                    # Name: 5, dtype: object
print("-----------------------------------------------------------------------------")
print("Function apply")
# apply our customised function to the column
print("The initial data frame")
print(df)
                    #    col_1  col_2    col_3
                    # 1      1    111    alpha
                    # 2      2    222    bravo
                    # 3      3    333  charlie
                    # 4      4    111      NaN
                    # 5      5    555      NaN
print()
print()
def mulby2(value): return value*2
# Broadcasting value using apply
df['col_1'] = df['col_1'].apply(mulby2)
print(df)
                    #    col_1  col_2    col_3
                    # 1      2    111    alpha
                    # 2      4    222    bravo
                    # 3      6    333  charlie
                    # 4      8    111      NaN
                    # 5     10    555      NaN
df['col_1'] = df['col_1'].apply(lambda x : m.sqrt(x))
print()
print(df)
                    #       col_1  col_2    col_3
                    # 1  1.414214    111    alpha
                    # 2  2.000000    222    bravo
                    # 3  2.449490    333  charlie
                    # 4  2.828427    111      NaN
                    # 5  3.162278    555      NaN

# def    square(x): return x*x
# lambda     x    :        x*x
print("-----------------------------------------------------------------------------")
print("Find the length of the string in column 3 ")
print(df['col_3'].str.len())
                    # 1    5.0
                    # 2    5.0
                    # 3    7.0
                    # 4    NaN
                    # 5    NaN
                    # Name: col_3, dtype: float64

print(df['col_3'].str.len()[3])
                    # 7.0
print("-----------------------------------------------------------------------------")
print("Create new column")
df['tejas'] = [1,2,3,4,5]
print(df)
# Create new column
#       col_1  col_2    col_3  tejas
# 1  1.414214    111    alpha      1
# 2  2.000000    222    bravo      2
# 3  2.449490    333  charlie      3
# 4  2.828427    111      NaN      4
# 5  3.162278    555      NaN      5

print("The index of the data frame are",df.index)
print("The columns of the data frame are",df.columns)
print()
print()
print("Dropping column 'tejas' ")
df.drop(['tejas'], axis = 1 , inplace = True)
print(df)
print("-----------------------------------------------------------------------------")
print("Pivot Table")
df['col_1'] = df['col_1'].apply(lambda x : x*x )
print(df.pivot_table(values = 'col_2', index = 'col_1',columns = 'col_3'))
# The elements of col_2 will be the values
# The elements of 'Col_1' will become the rows
# THe elemets of 'Col_3' will bwcome the columns
                    # col_3  alpha  bravo  charlie
                    # col_1
                    # 2.0    111.0    NaN      NaN
                    # 4.0      NaN  222.0      NaN
                    # 6.0      NaN    NaN    333.0
print()
print()
print(df.pivot_table(values = 'col_1', index = 'col_3',columns = 'col_2'))
                    # col_2    111  222  333
                    # col_3
                    # alpha    2.0  NaN  NaN
                    # bravo    NaN  4.0  NaN
                    # charlie  NaN  NaN  6.0
                    
# print(df.pivot_table(values = 'col_3', index = 'col_2',columns = 'col_1'))
# It gave an error because pivot aggregates only numeric data
print("---------------------------------------------------------------------------------")
# Creating DataFrame
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

foobar = pd.DataFrame(data)
print(foobar.pivot_table(values = 'D',index = ['A','B'],columns = 'C'))
                    # C          x    y
                    # A   B
                    # bar one  4.0  1.0
                    #     two  NaN  5.0
                    # foo one  1.0  3.0
                    #     two  2.0  NaN
