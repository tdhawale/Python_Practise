# -------------------------------------------------------------------------
# input always save the valu in string format so the result will be
# concatenation of x and y . But we want to add two integer number
x = input("Enter first numer: ")
y = input("Enter second numer: ")
z = x + y
print("The addition is:", z)
# -------------------------------------------------------------------------
# Now this will give a correct integer addition
x = int(input("Enter first numer: "))
y = int(input("Enter second numer: "))
z = x + y
print("The addition is:", z)
# -------------------------------------------------------------------------
# To take a single character as an input
ch = input("Enter a character:")[0]
print(ch)
ch1 = input("Enter a character:")
print(ch1[0])
# -------------------------------------------------------------------------
# eval evaluates only arithmetic functions
result = eval(input("Enter an expression:"))
print(result)
