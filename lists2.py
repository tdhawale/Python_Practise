print("Learning Lists in this tutuorial")
COVID = [14, 10, 99, 111, 34, 22]
print("Main List")
print(COVID)
# Printing the values at particular index
print("Printing the list based on index")
print("-------------------------------------------------------------------------------")
print("Value at index 1:", COVID[1])
print("Value at index -1:", COVID[-1])
print("Value at index -5:", COVID[-5])
# Printing the values from a range
print("The Values from range 1 to 4 is : ", COVID[1:5])
print("The Values from negative index : ", COVID[-5:-1])
# print("The Values from negative index : ", COVID[-5:-1]) It cant be from COVID[-1:-5] ir reverse order
# It is always in the fprward order
print("The Values from range 2 to remaining elements is : ", COVID[2:])
print("The Values from range 3 to remaining elements is : ", COVID[3:])
print("The Values from beginning upto index 3 : ", COVID[:4])
print("-------------------------------------------------------------------------------")
# The index values in the reverse format
print("The Index and the the elements in the list with negative index")
print("The last element is at index -1 : ", COVID[-1])
print("The element at index -2 : ", COVID[-2])
print("The element at index -3 : ", COVID[-3])
print("The element at index -4 : ", COVID[-4])
print("The element at index -5 : ", COVID[-5])
print("The first element is at index -6 : ", COVID[-6])
print("-------------------------------------------------------------------------------")
# The index value
print("The Index and the the elements in the list with positive index")
print("The element at index 0(The first element) : ", COVID[0])
print("The element at index 1(The second element) : ", COVID[1])
print("The element at index 2(The third element) : ", COVID[2])
print("The element at index 3(The fourth element) : ", COVID[3])
print("The element at index 4(The fifth element) : ", COVID[4])
print("The element at index 5(The last element) : ", COVID[5])
print("-------------------------------------------------------------------------------")
print("Changing/Modifying items")
COVID[1] = 'Value changes'
print(COVID)
print("-------------------------------------------------------------------------------")
print("Looping through the list")
for x in COVID:
    print("The Element is ", x)
print("-------------------------------------------------------------------------------")
print("Checking existence of element 14")
if 14 in COVID:
    print("Element exist")
else:
    print("Element does not exist")
print("-------------------------------------------------------------------------------")
print("The Length of the list is :", len(COVID))
print("-------------------------------------------------------------------------------")
print("Addidng items to the list :", COVID)
# append adds the value at the end of the list
COVID.append(19)
COVID.append(18)
# insert is used to add at a specific index
print("The list after append :", COVID)
COVID.insert(1, 69)  # addong element at second position i.e at index 2
print("List after inserting new value",
      COVID[1], " at second position :", COVID)
print("-------------------------------------------------------------------------------")
# Remove is used to remove a particular value
print("Remove items from the list")
COVID.remove("Value changes")
print("List after removing 'Value Changes' from the list :", COVID)
# Pop is used to remove the first element
print("Pop command removes the elememt on top of the stack(in this case) :", COVID.pop())
print("List after removing the element using pop:", COVID)

# Copying the lisr
COVID_TEMP1 = COVID.copy()
COVID_TEMP2 = list(COVID)

print("Temporary list 1:", COVID_TEMP1)
print("Temporary list 2:", COVID_TEMP2)
# Clear method empties the list
COVID_TEMP1.clear()
print("Clear empties  the temporary list 1:", COVID_TEMP1)
print("Main list:", COVID)      # why is the main list also getting empty

# delete is used to remove the index from the list
del COVID_TEMP2[2:4]
print("List after removing the elements from index 2 and index 3 :", COVID_TEMP2)
del COVID_TEMP2
# print("Values after deleting temporary list:", COVID_TEMP2)
# The execution of above statement will result error as the list is deleted
print("-------------------------------------------------------------------------------")
print("Joining the list")
COVID_TEMP3 = ["This is the list which will be joined", "with the main list"]
COVID_TEMP2 = COVID + COVID_TEMP3
print("Joining two lists", COVID_TEMP2)
print("-------------------------------------------------------------------------------")
# Extend is used to add values to the list
COVID.extend([999, 888, 777, 666])
print("Extending List", COVID)
del COVID_TEMP1
# Another way to create a list. Note the round brackets
COVID_TEMP1 = list((123, 456, 789))
COVID_TEMP1.extend(COVID)
print("The Extended new list :", COVID_TEMP1)
