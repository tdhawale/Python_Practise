import math as m
# If you want to import only specific function you can do it using
# from math import sqrt , pow
# here I have used alias for math library.You can call the function
# without alias by math.ceil(2.6)
print("The ceil value of 3.8 is :", m.ceil(3.8))
print("The floor value of 3.8 is :", m.floor(3.8))
print(m.pi)  # value of Pi
print(m.e)  # value of Epsilon
print(m.exp(3))  # e^3 [e raised to 3]
print(m.pow(3, 4))  # it is 3 to power of 4
# it is similar to 3*3*3*3
sqrt = m.sqrt(25)
print("The square root of 25 is :", sqrt)


print("The factorial of 4 is :", m.factorial(4))
result = eval(input("Enter an expression : "))
print("The value of result is ", result)
