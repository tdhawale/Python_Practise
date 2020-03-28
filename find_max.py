from numpy import *
n = int(input("Enter the size of array : "))
arr = array([], int)
print("Please Enter the elements in array : ", end="")
for i in range(n):
    arr = append(arr, [int(input())])
print(arr)

maximum = 0
for i in arr:
    if i >= maximum:
        maximum = i

print("The maximum value the array is :", maximum)
