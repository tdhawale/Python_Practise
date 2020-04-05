print("In this tutorial we will study about Lambda fucntion, and built in fucntions like filter and map")
# list comprehension is mainly used with lists . You can also use lambda functions for list .
# Example we had an tutorial for list comprehension where we used a list comprehension for creating
# a list that contains the even number . We could have also used a lambda function there.
info = input("Do you want to see information about lambda funtion(Y/N)")
if info == 'Y' or info == 'y':
	print("Information On Lambda Funtions")
	print("Lambda Functions also known as anonymous function are functions that is defined without a name.")
	# While normal functions are defined using the def keyword, in Python anonymous functions are defined using the
	# lambda keyword.
	print("Syntax of Lambda Function in python is : lambda arguments: expression ")
	print("Lambda functions can have any number of arguments but only one expression.\nThe expression is evaluated and"
	      " returned. Lambda functions can be used wherever function objects are required.")
	print()
	print("When to use lambda function:\nWe use lambda functions when we require a nameless function for a short period "
	      "of time.\nIn Python, we generally use it as an argument to a higher-order function(a function that takes in "
	      "other functions as arguments)\nLambda functions are used with builtin functions like filter(),map(),etc\n"
	      "\nThe filter function in Python takes in a function and a list as arguments.The function is called with all "
	      "the items in the list and a new list is returned which contains items for which the function evaluats = True"
	      "\n\nThe map function in Python takes in a function and a list.The function is called with all the items in "
	      "the list and a new list is returned which contains items returned by that function for each item.")
	
	
def square(x):
	return x*x

sq = square(5)
print("The square value is :",sq)

# so the abour line of code can also be written as
# def square(x): return x*x
# sq = square(5)
# Now we can use Lambda function for it
# def    square(x): return x*x
# lambda     x    :        x*x

del sq
# lambda function has no name . Assign it to a variable and then use
# the variable by passing different arguments to the variable
sq = lambda x : x*x
print("The square value using lambda function is :",sq(4))


print("---------------------------------------------------------------------------------------------------------")
even = list(filter(lambda x: (x%2 ==0 and x%5 ==0),range(100)))
print("The list of even numbers is :",even)
odd = list(filter(lambda x: (x%2 !=0 and x%5 ==0),range(100)))
print("The list of odd numbers is :",odd)
print("---------------------------------------------------------------------------------------------------------")
# map is a function with 2 arguements . A function and a sequence(list)
# performs a function for every element in a sequence
even_square = list(map(lambda x: x*x,even))
print("The list of square of even numbers is :",even_square)

#map can be applied to one or more list as well
print("------------------------------------------------------------------------------------------")
print(list(map(lambda x,y: (x if x%3 ==0 else y ), even ,odd  )))
# Output [0, 15, 25, 30, 45, 55, 60, 75, 85, 90]