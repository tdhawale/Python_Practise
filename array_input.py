# ----------------------------------------------------------------------
# If you are writing import then you will have to specify
# array.array() to create an array
# ----------------------------------------------------------------------
# import array

# arr = array.array('i', [])
# print(arr)

# ----------------------------------------------------------------------
# If you are writing from array import * no need to use
# array.array() to create an array
# ----------------------------------------------------------------------
from array import *
arr = array('i', [])    # created and empty array
print(arr)

n = int(input("Enter the size of array : "))
print("Please tnter the elements in array : ", end="")
for i in range(n):
    arr.append(int(input()))
print(arr)

search = int(input("Enter the element to search: "))
if search in arr:
    print("The element", search, "exists in the array at index", arr.index(search))
else:
    print("Element not found")
