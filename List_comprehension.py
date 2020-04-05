# List Comprehension is used to crate a list and avoid the use of for loops
# Structure of list comprehension
# [expression for item in list]
#  num*num for num in even
# expression = num*num
# item = num
# list = even

even = [2, 4, 6, 8, 10]
print("The matrix of even numbers upto 10 is: ",even)
#-----------------------------------------------------------------------------------------
#you can also create a list using for loop
even_square = []
for num in even:
	even_square.append(num*num)

print("The matrix of square of even numbers is: ",even_square)
#-----------------------------------------------------------------------------------------
# You can create the same list using list comprehension
print("---------------------------------------------------------------------------------------------------------------")
del even_square
even_square = [num*num for num in even]
print("The matrix of square of even numbers using list comprehension is: ",even_square)
#-----------------------------------------------------------------------------------------
print("---------------------------------------------------------------------------------------------------------------")
# You can use the if condition to control the elements that go into the list
# Here we are using the if condition and the condition is such that if the division by
# 2 results in a remainder then it is a odd number and put it in the list
odd = [num for num in range(50) if num%2 != 0]
print("The list of first 50 odd numbers is : ",odd)

del even
even = [num for num in range(50) if num%2 == 0]
print("The list of even numbers is upto 50: ",even)
print("---------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------
# Print the even numbers upto 50 which is even and divisible by 2
even_div_by_5 = []
even_div_by_5 = [num for num in range(50) if num % 2 == 0 if num % 5 == 0]
print("The list of first 50 even numbers divisible by 5 is: ",even_div_by_5)
#-----------------------------------------------------------------------------------------
# the if condition can also be for expression
print("---------------------------------------------------------------------------------------------------------------")
obj = ["Even" if num % 2 == 0 else "Odd" for num in range(10)]
print("The number are : ", obj)
print("---------------------------------------------------------------------------------------------------------------")
# You can also use multiple for loops inside a list comprehension
print("Printing the trasnpose of a matrix")
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)

transpose_t = [[pow(row[i],2) if i%2 == 0 else pow(row[i],2) for row in matrix] for i in range(2)]
print(transpose_t)
#----------------------------------------------------------------------------------------------------------------------
