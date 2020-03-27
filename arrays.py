# We have list and tuple but why arrays
# we have all the values of same type. In list there can be elements
# of different types as well


# Lists are much more flexible than arrays.
# They can store elements of different data types including string.
#  Also, lists are faster than arrays.
# And, if you need to do mathematical computation on arrays and matrices,
# you are much better off using something like NumPy library.


# Arrays in python don't have specific size . We cann extend or shrink the array
# Code	C Type	                Python Type     	Min bytes
# 'b'	signed char	                int	            1
# 'B'	unsigned char               int	            1
# 'u'	Py_UNICODE	                Unicode	        2
# 'h'	signed short	            int	            2
# 'H'	unsigned short	            int	            2
# 'i'	signed int	                int	            2
# 'I'	unsigned int	            int	            2
# 'l'	signed long	                int	            4
# 'L'	unsigned long	            int	            4
# 'f'	float	                    float       	4
# 'd'	double	                    float	        8
import array as arr

a = arr.array('I', [1, 7, 89, 977, 65, 3, 54, 64])
b = arr.array('d', [1, 7, 89, 977, 65, 3, 54, 64])
# I cant use the below statement as i have imported array as arr
# b = array.array('d', [1, 7, 89, 977, 65, 3, 54, 64])
print(a)
print(b)
print("--------------------------------------------------------")
print("Accessing elements of array")
print("The first element of an array", a[0])
print("The second element of an array", a[2])
for i in a:
    print("The elements in an array", i)
print("--------------------------------------------------------")
print("Slicing an array : ", end="")
print(a[1:4])  # array elements from index 1 to index 3
print("--------------------------------------------------------")
# arrays are mutable and we can change the contents of the array
print("The elements in an array before updating are : [", end="")
for i in a:
    print("", i, end="")
print(" ]")

a[2] = 222
print("The elements in an array after updating are : [ ", end="")
length = len(a)
for i in range(length):
    if i == 0:
        print(a[i], end="")
    else:
        print(",", a[i], end="")
print(" ]")
#################################################################################
a[3:6] = arr.array('I', [333, 444, 555])
print(
    "The array after changing elements from index 3 to index 5 is : [", end="")
length = len(a)
for i in range(length):
    if i == 0:
        print(a[i], end="")
    else:
        print(",", a[i], end="")
print(" ]")
print("--------------------------------------------------------------------------")
a.append(5)
print("After adding element 5 to the array we get array : [", end="")
length = len(a)
for i in range(length):
    if i == 0:
        print(a[i], end="")
    else:
        print(",", a[i], end="")
print(" ]")
print("--------------------------------------------------------------------------")
a.extend([10, 11, 12])
print(
    "After appending elements 10,11 and 12 to the array we get array : [", end="")
length = len(a)
for i in range(length):
    if i == 0:
        print(a[i], end="")
    else:
        print(",", a[i], end="")
print(" ]")
print("--------------------------------------------------------------------------")
del a[3:5]
print("After deleting elements from index 3 and 4 we get array : [", end="")
length = len(a)
for i in range(length):
    if i == 0:
        print(a[i], end="")
    else:
        print(",", a[i], end="")
print(" ]")
print("--------------------------------------------------------------------------")
# copy one array into another array
a_temp = arr.array('I', a)
print("Temporary array 1", a_temp)

a_temp2 = arr.array(a.typecode, (i for i in a))
print("Temporary array 2", a_temp2)

a_temp2 = arr.array(a.typecode, (i*i for i in a))
print("Temporary array 3 which is a square", a_temp2)

# deleting array
del a_temp
# print(a_temp)         will result in error
print("--------------------------------------------------------------------------")
a.reverse()
print("After reversing array we get : [", end="")
length = len(a)
for i in range(length):
    if i == 0:
        print(a[i], end="")
    else:
        print(",", a[i], end="")
print(" ]")
print("---------------------------------------------------------------------------")
print("The number of times 222 occurs in the array is :", a.count(222))
# count is used ot count the number of occurence of an element
print("--------------------------------------------------------------------------")
# returns the current memory address and the length in elements of the buffer used to hold arrays contents.
print("The buffer address and the number of elements are:", a.buffer_info())
print("--------------------------------------------------------------------------")
print("The length of array using len function is :", len(a))
print("The length of array using buffer_info function is :",
      a.buffer_info()[1])
