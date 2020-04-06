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
del arr1 , arr2 , arr3
arr1 = arange(1, 25, 3)
print("The array 1 is : ",arr1)
arr2 = ones(5, int)
print("The array 2 is : ",arr2)
#Slicing an array
print("The first 3 elemets of array 1 are: ", arr1[0:3])        #arr1[inclusie:exclusive]

arr3 = 2*arr1.copy()
arr3_2d = arr3.reshape(4,2)
print("The 2d array is :", arr3_2d)
#Accessing the elements of the array
print("---------------------------------------------------------------------------------")
print("The 2nd element of the 3 row is :", arr3_2d[3][1])
print("The second row is:", arr3_2d[1])
print("---------------------------------------------------------------------------------")
print("Broadcasting in numpy array  ")
# Broadcasting the value 500 to the first 3 elements of the array
print("The array before bradcasting the values is: ",arr1)
arr1[1:4] = 500
print("The array after bradcasting the value 500 is: ",arr1)
print("---------------------------------------------------------------------------------")
print("Broadcasting 500 to the entire 2nd row of a 2D array")
print("The array before braodcasting the value 500 is :",arr3_2d)
arr3_2d[1] = 500
print("The array after braodcasting the value 500 is :",arr3_2d)
arr4 = arange(0,2) #arr4 = [0,1]
print(arr3_2d + arr4)  # See documentation of broadcasting for the addition
# https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html
# https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html
print(arr3_2d + 300)   # Every element is added with 300
array_2d = ones((4,4), int)
array_2d = array_2d + arange(0,4)
print(array_2d)
print("------------------------------------------------------------------------------------")
# array_2d = array_2d + [300,2] # Won't work because dimensions are not same
array_2d = array_2d + [300,2, 3,4]
print(array_2d)
print("------------------------------------------------------------------------------------")
print(arange(3))
print(arange(3).reshape(3,1))
print(arange(0,4).reshape(4,1))

arr_row = arange(3)     # one row with 3 elements [0,1,2]
arr_col = arange(3).reshape(3,1) # 3 rows each with one element [[0]
#                                                                [1]
#                                                                [2]]
# arr_col = arange(0,3).reshape(3,1)    # it means same as above
# another way to do it array_2 = np.arange(1,4)[:, np.newaxis]
print(arr_row + arr_col)
# arr_row will be        +             array column will be
# [0 1 2]                                   [0 0 0]
# [0 1 2]                                   [1 1 1]
# [0 1 2]                                   [2 2 2]
print("------------------------------------------------------------------------------------")
print("Indexing")
del array_2d
array_2d = zeros((5,4),int)          # Create a zero matrix
# using shape attribute, get the no to run the loop
for i in range(array_2d.shape[1]):  # using range() in the loop
    array_2d[i] = i

print("The number of rows in the array are:" , array_2d.shape[0])
print("The number of columns in the array are:" , array_2d.shape[1])

# Generaring a random 5x4 array without random.randint()
for i in range(array_2d.shape[0]) :
    for j in range(array_2d.shape[1]) :
        array_2d[i][j] = random.randint(1 , 50)

arr_randint = random.randint(1 , 100 , size = (4 , 4))  # (low,high, size(Matrix of size))
print("Multidimensional random array is: " , arr_randint)
print("The 2D array is \n",array_2d)
print()
print("Fancy Indexing ")
# array_name[[rows],[columns]] # if you want to print in single row
# arr1[[2,3]]
# prints all the elements of 1 and 2 row
# arr1[,[1,2]]
# array_name[from row: to row,from column: to column]
# eg arr1[:3,1:2]
print("The 2D array elements of 3 rd element in (2 and 3) row are:\n",array_2d[:2,2:])
print()
print("The 2D array elements of 2 and 3 row: \n",array_2d[[1,2]])
print()
print("The 2D array elements of 3 column are: \n",array_2d[:,[2]])
print()
# This index can be random as well . Need not be in sequence
print("The 2D array elements of 4th and 1st row are: \n",array_2d[[3,0]])
print()

print("----------------------------------------------------------------------------------------")
print("Boolean Masking")
#  It is used to count, modify, extract or manipulate values in an array based on certain condition or criteria
del arr1
arr1 = arange(1,11)
print("The array 1 is :", arr1)
bool_arr1 = arr1 > 3
print("The boolean array1 is:", bool_arr1)
arr1_cond = arr1[arr1 > 3]
print(arr1_cond)
del arr1_cond
arr1_cond = arr1[arr1%2 == 0]
print(arr1_cond)
print("----------------------------------------------------------------------------")
del arr1 , arr1_cond
arr1 = random.randint(1,24,size = (4,6))
print("The elements of array are :\n",arr1)
# Filtering array based on multiple conditions
mod_con = (arr1%2 == 0) & (arr1%5 == 0)
arr1_cond = arr1[mod_con]
print("The conditional array is :\n", arr1_cond)



