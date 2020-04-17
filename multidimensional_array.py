from numpy import *
# from array import *

# We can also create a single dimensional array using numpy
arr_numpy = ([1, 2, 3, 4, 5])
# you can aslo specify type but at the end which is different in the way
# that you specify type for a normal array
arr_numpy_type = ([1, 2, 3, 4, 5], float)
# arr_array_array = array('I', [1, 2, 3, 4, 5])
print("The array created using numpy library is :", arr_numpy)
print("The array created using numpy library of type float is :", arr_numpy_type)
# print("The array created using array library is :", arr_array_array)


# Different ways to create an array
# 1. function array()
# 2. function linespace()
# 3. function logspace()
# 4. function arange()
# 5. function zeros()
# 6. function ones()
cont = 'Y'

while cont == 'Y' or cont == 'y':
    print("There are 6 different wasys to create an array")
    print("1. function array()")
    print("2. function linespace()")
    print("3. function logspace()")
    print("4. function arrange()")
    print("5. function zeros()")
    print("6. function ones()")
    print("7. function eye()[prints identity matrix]")
    print("8. function random.rand()")
    view = int(input("Enter the type of array you want to view: "))
    if cont == 'Y' or cont == 'y':
        if view == 1:
            # Type 1 : Array()
            print("---------------------------------------------------------")
            print("Creating arrays using ARRAY() function")
            print("---------------------------------------------------------")
            print("Information on ARRAY() function is given below")
            print(
                "Remember the concept of array that all the values of an array should be of same type.")
            print(
                "But here we have 2.3 as float So entire array will be converted to float type")
            print()
            print()
            arr_array = array([1, 2, 3, 4, 5])
            print("The type of array is :", arr_array.dtype)
            print("The elements of array are :", arr_array)
            print("---------------------------------------------------------")
            # Remember the concept of array that all the values of an
            # array should be of same type . But here we have 2.3 as float
            # So entire array will be converted to float type
            arr_array_float = array([1, 2.3, 3, 4, 5])
            print("The type of array is :", arr_array_float.dtype)
            print("The elements of array are :", arr_array_float)
            print()
            cont = input("Do you want to continue (Y/N): ")
        elif view == 2:
            print("---------------------------------------------------------")
            print("Creating arrays using LINSPACE() function")
            print("---------------------------------------------------------")
            print("Information on LINSPACE() function is given below")
            print("Linspace takes 3 parameters--> START --> STOP --> STEP")
            print("If we don't specify step default will be 50.", end="")
            print("So it is dividing the array into 50 parts")
            print()
            print()
            print(
                "In range the stop is not included in the calculation but in linspace the stop is inchluded")
            print("if range(0,15) --> it will take from 0 to 14(total value will be 15)")
            print(
                "if linspace(0,15) --> it will take from 0 to 15(total valuse will be 16)")
            print("linspace will store the values in float format always")
            print()
            print()
            # linspace takes 3 parameters--> START --> STOP --> STEP

            # if we don't specify step default will be 50. So it is dividing the array
            # into 50 parts
            arr_linspace = linspace(0, 15)
            print("The elements of linspace array without step condition are:")
            print(arr_linspace)

            # In range the stop is not included in the calculation
            # but in linspace the stop is inchluded i.e
            # if range(0,15) --> it will take from 0 to 14(total value will be 15)
            # if linspace(0,15) --> it will take from 0 to 15(total valuse will be 16)
            # linspace will store the values in float format always
            print("----------------------------------------------------------")
            arr_linspace = linspace(0, 15, 16)
            print("The type of linspace array is: ", arr_linspace.dtype)
            print("The elements of linspace array are:", end="")
            print(arr_linspace)
            # retstep sspecifies the length of the step
            arr_linspace = linspace(0 , 15 , 16, retstep = True)
            print("The elements of linspace array along with its step size are:" , end = "")
            print(arr_linspace)
            print()
            arr_linspace = linspace(0 , 15 , 31, retstep = True)
            print("The elements of linspace array along with its step size are:" , end = "")
            print(arr_linspace)
            print()
            cont = input("Do you want to continue (Y/N): ")
        elif view == 3:
            print("---------------------------------------------------------")
            print("Creating arrays using LOGSPACE() function")
            print("---------------------------------------------------------")
            print("Information on LOGSPACE() function is given below")
            print("The difference between two numbers will be same in linspace")
            print(
                "But in logspace the difference between two numbers will depend on the log of the numbers")
            print(
                "It will start from 10 raised to 1 and the last number will be 10 raised to 10")
            # The difference between two numbers will be same in linspace
            # but in logspace the difference between two numbers will depend on the
            # log of the numbers
            # It will start from 10 raised to 1
            # and the last number will be 10 raised to 10
            arr_logspace = logspace(1, 10, 5)
            print("The type of array is : ", arr_logspace.dtype)
            print("The elements of array created using LOGSPACE() are:", end="")
            print(arr_logspace)
            # print("The elements of array created using LOGSPACE() are: %.2f", % arr_logspace)
            # .xf specifies how much numbers after point
            # first element will be 10 raised to 1
            print("The first element is ", '%.2f' % arr_logspace[0])
            # last element will be 10 raised to 10
            print("The last element is ", '%.4f' % arr_logspace[4])
            print()
            cont = input("Do you want to continue (Y/N): ")
        elif view == 4:
            print("---------------------------------------------------------")
            print("Creating arrays using ARANGE() function")
            print("---------------------------------------------------------")
            print("Information on Linspace() function is given below")
            print("Here we specify -->START -->STOP -->STEP")
            print(
                "But here in contrast of linspace where the array is divided into step parts")            # here we specify -->START -->STOP -->STEP
            print("Here in arange() the array is incremented by step parts")
            print()
            print()
            # but here in contrast of linspace where the array is divided into
            # step parts , here in arange() the array is incremented by step parts
            arr_arange = arange(1, 20, 3)
            print("The type of array is :", arr_arange.dtype)
            print("The elements of array created using ARANGE() are:", arr_arange)
            print()
            cont = input("Do you want to continue (Y/N): ")
        elif view == 5:
            print("---------------------------------------------------------")
            print("Creating arrays using ZEROS() function")
            print("---------------------------------------------------------")
            # Creates a one dimenstional array with 5 zeros
            arr_zeros = zeros(5, int)
            print("The elements of array created by ZEROS() are:", arr_zeros)
            print()
            del arr_zeros
            arr_zeros = zeros((4,6),int)
            print("The elements of 2D array created by ZEROS() are:" , arr_zeros)
            print()
            cont = input("Do you want to continue (Y/N): ")
        elif view == 6:
            print("---------------------------------------------------------")
            print("Creating arrays using ONES() function")
            print("---------------------------------------------------------")
            arr_ones = ones(5)
            print("The default type will be float")
            print(
                "The elements of array created by ONES() are[default type float]:", arr_ones)
            # Creating an array of type int
            arr_ones = ones(5, int)
            print("The elements of array created by ONES() are:", arr_ones)
            print()
            cont = input("Do you want to continue (Y/N): ")
        elif view == 7 :
            arr_identity = eye(4)
            print("The identity matrix is: ",arr_identity)
            cont = input("Do you want to continue (Y/N): ")
        elif view == 8 :
            arr_rand = random.rand(1)
            print("The random array with 1 elements is: " , arr_rand)
            arr_rand = random.rand(3)
            # prints 3 random values between 0 and 1
            print("The random array with 3 elements is: ",arr_rand)
            del arr_rand
            arr_rand = random.rand(3,2)
            print("The random array with 3 rows and 2 colums is: ",arr_rand)
            # Randn return a simple form of standard normal or gaussian distribution
            arr_randn = random.randn(4,4)
            print("The random array with 4 rows and 4 colums is: " , arr_randn)
            
            #Randint generates a random variable between the specififed range
            arr_randint = random.randint(1,100)             # default size 1 i.r only one element
            print(("The random array", arr_randint))
            del arr_randint
            arr_randint = random.randint(1,100,size = (4,4))   #(low,high, size(Matrix of size))
            print("Multidimensional random array is: ", arr_randint)
            cont = input("Do you want to continue (Y/N): ")
    else:
        break
