from numpy import *

arr1 = array([1, 3, 4, 6, 7, 9])
print("----------------------------------------------------")
print("Operations on array")
print("THe initial array is: ", arr1)
# 5 will be added to every element
arr1 = arr1 + 5
print("The first array after addiing 5 to each element is: ", arr1)
print("The sum of elements of array 1 is: ", sum(arr1))
print("----------------------------------------------------------------")
arr2 = arr1
print("The first array is", arr1)
print("The second array is", arr2)
arr3 = arr1 + arr2
print("The addition of two arrays is :", arr3)
print("The square root of elements of the array 1", sqrt(arr1))
print("The sin values of elements of the array 1", sin(arr1))
print(arr1)
print("The maximum element of the array1 is",
      max(arr1), "at index",  where(arr1 == max(arr1)))
print("The length of array1 is :", len(arr1))
print("----------------------------------------------------------------")
print(concatenate([arr1, arr2*2]))

############################################################################
# Copying an array
############################################################################
del arr1, arr2, arr3

arr1 = array([1, 33, 85, 2, 7, 52])
arr2 = arr1
print("----------------------------------------------------------------")
print("The first array is :", arr1, "and has address", id(arr1))
print("The second array is :", arr2, "and has address", id(arr2))
# here both the arrays are pointing to same location and has same address
arr1 = append(arr1, [1])
print("The first array is :", arr1, "and has address", id(arr1))
print("The second array is :", arr2, "and has address", id(arr2))

print("----------------------------------------------------------------")
# What if i want two same arrays but with different addresses
# view() creates a shallow copy i.e arr1 and arr3 have same values
# but have different address. If I change the value of arr1
# the value of arr3 will also change
print("view() creates a shallow copy")
arr3 = arr1.view()
print("The first array is :", arr1, "and has address", id(arr1))
print("The third array is : ", arr3, "and has address", id(arr3))

arr1[0] = 00
print("The first array after change in arr1 is :",
      arr1, "and has address", id(arr1))
print("The third array after change in arr1 is  is : ",
      arr3, "and has address", id(arr3))
print("----------------------------------------------------------------")
# What if i want two same arrays but with different addresses
# copy() creates a deep copy i.e arr1 and arr3 have same values
# but have different address. If I change the value of arr1
# the value of arr3 will not be affected
# copy() used in list tuples dictonarites set but not in array library
print("copy() creates a deep copy")
del arr3
arr3 = arr1.copy()
print("The first array is :", arr1, "and has address", id(arr1))
print("The third array is : ", arr3, "and has address", id(arr3))
arr1[0] = 77
print("The first array after change in arr1 is :",
      arr1, "and has address", id(arr1))
print("The third array after change in arr1 is  is : ",
      arr3, "and has address", id(arr3))
