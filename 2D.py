from numpy import *

arr1 = array([[1, 22, 3],
              [5, 6, 7]

              ])

print(arr1)
print("The type of array is", arr1.dtype)
print("The size of array is", arr1.size)
print("The dimension of array are:", arr1.ndim)
print("The dimension of the array is :",arr1.shape)
# -------------------------------------------------------------------------------------
# From 2D array create a 1D array
print("--------------------------------------------------------------------------------")
arr2 = arr1.flatten()
print("The contents of array 1 are:", arr1)
print("The contents of array 2 which is 1D array are:",arr2)
# -------------------------------------------------------------------------------------
# From 1D array create 3D array
arr3 = arr2.reshape(3,2)
print("The 3D array is :", arr3)
# -------------------------------------------------------------------------------------
del  arr1 , arr2
arr1 = array([[1, 22, 3, 6, 2, 1],
                    [5, 6, 7, 4, 7, 2]
              ])
print("--------------------------------------------------------------------------------")
print("The array before it is reshaped",arr1)
print("The 3D array generated is ",arr1.reshape(2,2,3))
print("--------------------------------------------------------------------------------")
# Converting an 2D array into a matrix
del  arr1
arr1 = array([[1,8],[4,2]])
arr2 = 3*arr1.copy()
print("The firse array",arr1)
print("The second array",arr2)
print("Converting a 2D array into a matrix and then performing multiplication")
mat1 = matrix(arr1)
mat2= matrix(arr2)
mat3 = mat1*mat2
print("The matrix after multiplication is :",mat3)
print("--------------------------------------------------------------------------------")
print("The diagonal elements of matrix are: ",diagonal(mat3))
print("The min element is: ",mat3.min(),"at index",mat3.argmax())
print("The max element is: ",mat3.max(),"at index",mat3.argmin() )
print("--------------------------------------------------------------------------------")




