# set1 uses a concept of hash and it stores the value in random fashion.
# set1 does not support duplicate values

set1 = {12, 2335, 4576, 124, 658, 586, 12}
print(set1)
# print(s[2]) .......set1 also does not support indexing
print("--------------------------------------------------------------------------------")
print("Since the set1 is not indexed, you cant access the set1 using index values")
for x in set1:
    print("The elements of set1:", x)
print("--------------------------------------------------------------------------------")
# Same like that in list
if 12 in set1:
    print("Element 12 exists")
else:
    print("Element does not exists")
print("--------------------------------------------------------------------------------")
# example can be adhar card number or SSN number
print("Once the set1 is created you cannot change its items, but can add new items")
# To add items to the set1 use add(). Add is used to add a single element to the set1
# It is same like append or inser(idex, value) in list
set1.add(999)
print("The set1 after addition is :", set1)
print("--------------------------------------------------------------------------------")
# To add multiple values to the set1 use update.
# It is is same like extend in list
set1.update([111, 222, 333])
print("The list after updating multiple values is :", set1)
print("--------------------------------------------------------------------------------")
# length of the set1 in the same way as that of the lise
print("The number of items in the set1 is :", len(set1))
print("--------------------------------------------------------------------------------")
set1.pop()
print("The set1 after poping the top of the stack is :", set1)
# remove item from the set1
# If the item to remove does not exist, remove() will raise an error.
set1.remove(111)
print("The set1 after removing element 111 is :", set1)
# discard
set1.discard(123)
print("The set1 after removing element 123 is :", set1)

# The difference between set1 and discard is that if the element is not there in the
# list remove will give runtime error while discard won't give runtime error
print("--------------------------------------------------------------------------------")
set1_temp = set1.copy()
print("Temporary set1 before clearing", set1_temp)
# Empty the set1
set1_temp.clear()
print("Temporary set1 after clearing :", set1_temp)
print("--------------------------------------------------------------------------------")
# delete the set1
del set1_temp
# print("Temporary set1 after clearing :", set1_temp)
# the above command will give runtime error because the set1 was deleted

set1_temp = {123, 456, 789}
set1 = set1.union(set1_temp)
print("The set1 after union is :", set1)
print("--------------------------------------------------------------------------------")
# print("Joining the list")
# COVID_TEMP3 = ["This is the list which will be joined", "with the main list"]
# COVID_TEMP2 = COVID + COVID_TEMP3
# update
set1_temp2 = {123, 456, 1456}
set1.update(set1_temp2)
print("The set1 after update is :", set1)
# Both union() and update() will exclude any duplicate items.
print("--------------------------------------------------------------------------------")
# Another way to create a list. Note the round brackets
# COVID_TEMP1 = list((123, 456, 789))
# create a new set1
new_set = set((1, 2, 3))
print("The new set1 is :", new_set)
