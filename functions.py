def calc(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    return add , sub , mul
 # We can return multiple values in function
 # There is not pass by value and pass by refrence in python
r1,r2,r3 = calc(10,5)

print("The addition is :", r1)
print("The subtraction is :", r2)
print("The multiplication is :", r3)

# Pass by value : You are passing the value
# Pass by refrence : You are passing the address
# Refrence video : https://www.youtube.com/watch?v=ijXMGpoMkhQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=37

# In python we don't have pass by value and pass by refrence
def update_pass_by_value(x):
    x = 8
    print()
    print("The value of x is :",x)
    print("The address of x is :",id(x))
 # 1. pass by value
a = 10
print("-----------------------------------------------------------")
print("Checking for Pass by value")
print("The address of a is :", id(a))
print("The address of 8 is :", id(10))
update_pass_by_value(a)       # we are simply passing the value
print("The address of a is ", id(a),"and the value of a is ", a)
# In this case since we are passing the value to function update,
# update in the variable x does not update the value of a
print("-----------------------------------------------------------")
def update_pass_by_reference(x):
    x = 8
    print()
    print("The value of x is :" , x)
    print("The address of x is :" , id(x))

a = 10
print("-----------------------------------------------------------")
print("Checking for Pass by reference")
print("The address of a is :", id(a))
print("The address of 8 is :", id(10))
update_pass_by_value(id(a))       # we are simply passing the value
print("The address of a is ", id(a),"and the value of a is ", a)
print("-----------------------------------------------------------")
def fun(param = 1):
    print("The parameter value is {} which is passed as input".format(param))

fun()   # if no value is passed it will take the default value
#above statement output will be-->The parameter value is 1 which is passed as input
fun(19) # if some value is passed then it will take the passed value
#above statement output will be-->The parameter value is 19 which is passed as input