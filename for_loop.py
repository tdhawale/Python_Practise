# A for loop is used for iterating over a sequence
# (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like a for loop in other programing languages but more like
# an iterator
print("-------------------------------------------------------------")
print("Loopint through a list")
ludwigstrasse = ["Tejas", "Sujay", "Mohit"]
print("The members in the house are")
for x in ludwigstrasse:
    print(x)
print("-------------------------------------------------------------")
print("Loopint through a string")
for x in "TEJAS":
    print(x)
print("-------------------------------------------------------------")
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
print("Printing the values for range(6):")
for x in range(6):
    print(x)
print("-------------------------------------------------------------")
# you can also start from some different values
# it will start from 2 and end on 7
print("printing the values for range(2,8):")
for x in range(2, 8):
    if x == 6:
        continue
    print(x)
print("-------------------------------------------------------------")
# The default increment of for function is 1. You can also change it
#  by specifying the third parameter range(2,30,3) where 3 indicates
#  that the value will be incremented by 3
print("printing the values for range(2,30,3):")
for x in range(2, 30, 3):
    if x >= 24:
        break
    print(x)
print("-------------------------------------------------------------")
