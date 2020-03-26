# One method to swap variable is using another variabl
print("--------------------------------------------------------")
print("Using the conventional method for swap")
a = 5
b = 6
print("The value of a before swap is :", a)
print("The value of b before swap is :", b)
temp = a
a = b
b = temp
print("The value of a after swap is :", a)
print("The value of b after swap is :", b)
print("--------------------------------------------------------")
print("Swapping without using extra variable")
a = 5  # 101  value in binary
b = 6  # 110  value in binary
print("The value of a before swap is :", a)
print("The value of b before swap is :", b)
a = a + b   # the addition is 11 which will require extra bits 1011
b = a - b
a = a - b
print("The value of a after swap is :", a)
print("The value of b after swap is :", b)

print("--------------------------------------------------------")
print("Swapping without using extra variable and without wasting extra bits")
a = 5
b = 6
print("The value of a before swap is :", a)
print("The value of b before swap is :", b)
a = a ^ b  # we are using XOR here
b = a ^ b
a = a ^ b
print("The value of a after swap is :", a)
print("The value of b after swap is :", b)
print("--------------------------------------------------------")
print("Swapping without using ROT_TWO(Swaps the top most stack items)")
a = 5
b = 6
print("The value of a before swap is :", a)
print("The value of b before swap is :", b)
a, b = b, a  # this works only if it written in the same line
# the values will be assigned from right to left . i.t right hand side will be solved first
# b(top of stack) will be assigned the value of a(top of stack)
# a(top of stack) will be assigned the value of b(top of stack)
# to get more information on this search for ROT_TWO() in python
print("The value of a after swap is :", a)
print("The value of b after swap is :", b)
