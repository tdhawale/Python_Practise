import numpy as np
import pandas as pd

my_label = ['x','y','z']
my_data = [100,200,300]
ser1 = pd.Series(data = my_data)
print("The Series created from Dictionary is:") # Here the labels will be automatically assigned to 0,1,2
print(ser1)
					# The Series created from Dictionary is:
					# 0    100
					# 1    200
					# 2    300
					# dtype: int64
print("-----------------------------------------------------------------")
ser = pd.Series(data = my_data, index = my_label)
print("The Series created from List is:")  # Here my specified labels will be assigned
print(ser)
					# The Series created from List is:
					# x    100
					# y    200
					# z    300
					# dtype: int64
print("-----------------------------------------------------------------")
# Create series using numpy array
arr1 = np.array(my_data)
ser = pd.Series(data = arr1, index = my_label)
print("The Series created from array is:")
print(ser)
					# The Series created from array is:
					# x    100
					# y    200
					# z    300
					# dtype: int32
print("-----------------------------------------------------------------")
# Dictionaries are very useful with pandas
# Pandas take the keys as labels
dict = {'x': 100, 'y':200, 'z' :300}
ser_dict = pd.Series(dict)
print("The Series created from Dictionary is:")
print(ser_dict)
					# The Series created from Dictionary is:
					# x    100
					# y    200
					# z    300
					# dtype: int64
print("----------------------------------------------------------------")
# If we use dictionary the series is sorted based on the key values
dict_usa = {'Total Cases':339131,'Total Deaths':9689,'Total Recovered':18029,'Active Cases':952930,'Major City Affected'
			:'New York'}

dict_spain = {'Total Cases':135032,'Total Deaths':13169,'Total Recovered':40437,'Active Cases':81426}
dict_italy = {'Total Cases':128948,'Total Deaths':15887,'Total Recovered':21815,'Active Cases':91246}
dict_germany = {'Total Cases':100770,'Total Deaths':1608,'Total Recovered':28700,'Active Cases':70462,'Most affected '
                                                                                                      'State' : 'NRW'}
ser_usa = pd.Series(dict_usa)
ser_spain = pd.Series(dict_spain)
ser_italy = pd.Series(dict_italy)
ser_germany = pd.Series(dict_germany)
print("--------------------------------------------------------------------------------------")
print("COVID-19 updates for USA")
print(ser_usa)
print("--------------------------------------------------------------------------------------")
print("COVID-19 updates for Spain")
print(ser_spain)
print("--------------------------------------------------------------------------------------")
print("COVID-19 updates for Italy")
print(ser_italy)
print("--------------------------------------------------------------------------------------")
print("COVID-19 updates for Germany")
print(ser_germany)
					# COVID-19 updates for USA
					# Total Cases              339131
					# Total Deaths               9689
					# Total Recovered           18029
					# Active Cases             952930
					# Major City Affected    New York
					# dtype: object
					#
					# COVID-19 updates for Spain
					# Total Cases        135032
					# Total Deaths        13169
					# Total Recovered     40437
					# Active Cases        81426
					# dtype: int64
					#
					# COVID-19 updates for Italy
					# Total Cases        128948
					# Total Deaths        15887
					# Total Recovered     21815
					# Active Cases        91246
					# dtype: int64
					#
					# COVID-19 updates for Germany
					# Total Cases            100770
					# Total Deaths             1608
					# Total Recovered         28700
					# Active Cases            70462
					# Most affected State       NRW
					# dtype: object
print("--------------------------------------------------------------------------------------")
print("The number of cases in germany are: {}".format(ser_germany['Total Cases']))
print("--------------------------------------------------------------------------------------")
# The keys are arranged in sorted order
print("The addition of USA and Germany cases are", ser_germany+ser_usa)
# The addition add the values for the common keys present. For the keys which are not present
# it shows NaN[which is considered in pandas as missing data]
print("--------------------------------------------------------------------------------------")
print("The total number of cases are", ser_germany['Total Cases']+ser_usa['Total Cases']+ser_italy['Total Cases']+
      ser_spain['Total Cases'])
print("--------------------------------------------------------------------------------------")
# Is null return true if it doesn't find the value
# Not null returns true if the value is present
print( "Is Null method:\n",(ser_germany+ser_usa).isnull())
# So in the above statement since the most state is NaN , it is null and so it shows true
print("--------------------------------------------------------------------------------------")
print( "Not Null Method:\n",(ser_germany+ser_usa).notnull())
print("--------------------------------------------------------------------------------------")
# axes: returns list of the row axis labels/index
# values: returns list of values/data
print("The keys of series Covid_germany are:",ser_germany.axes,"\nAnd its values are",ser_germany.values)
print()
print("The keys of series 1 are:",ser1.axes,"\nAnd its values are:",ser1.values) # [RangeIndex(start=0, stop=3, step=1)]   -----> Default labels
print("--------------------------------------------------------------------------------------")

print("The first element of the series Covid Germany is:",ser_germany.head(1)[0])
print("And the last element is:",ser_germany.tail(2)[0]) # [0] to remove the type ehich was also being printed
print()
# Shows the first three elements
print("The first 3 elemets series Covid Germany is:\n",ser_germany.head(3))
print("The last 2 elements of series Covid Germany is:\n",ser_germany.tail(4))

print("--------------------------------------------------------------------------------------")
# To check the number of elements in your data.
print("The shape of the series is:", ser_germany.shape)
print("The size of the series is:", ser_germany.size)
print("Is the series COVID Germany empty?", ser_germany.empty)
					# The shape of the series is: (5,)
					# The size of the series is: 5
					# Is the series COVID Germany empty? False