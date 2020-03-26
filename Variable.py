# This will file will show the address of a variable
a = 10
print("The address of a is :", id(a))
b = 20
print("The address of b is :", id(b))
c = a
print("The address of c is :", id(c))
print("The address of 10 is :", id(10))
# so python is more efficient because it does not have different boxes or
# different address for variables which have same value
# here variable a , c have the same value. so it will point to the same address
