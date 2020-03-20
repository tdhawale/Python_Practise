#List is mutable and we can change the values
from builtins import min

fruits = ["Apple","Mango","Banana","Carrot"]
print("**************************************************")
print("Printing the entire List")
print(fruits)
#print('\n')
print("**************************************************")
print("Printing the Specific list item")
print(fruits[2])
fruits.append("Guava")
fruits.append("Lichi")
print("**************************************************")
print("Printing the List from specified Index")
print(fruits)
print(fruits[2:5])      # Prints elements of the list from index 1 to 4
print(fruits[2:6])      # Prints elements of the list from index 2 to index 5()
print(fruits[1:])       # Prints all the list element from 1 till the end of the list
#print(fruits[-5])       # Prints array in backward direction
###############################################################
#We can even make lists of uncommon elements like string and intgers
container = [3,"Mita",4,"Babita"]
print(container)
###############################################################
chinchwad = ["Ramesh","Suresh","Hitesh","Ritesh"]
pimpri = ["Anita","Vanita","Babita","Savita"]
staff = [chinchwad , pimpri]
print("**************************************************")
print("Printing the staff details")
print(staff)

print("**************************************************")
print("Sorting the staff members at chinchwad")
chinchwad.sort()
print(chinchwad)

#insert is used to insert at a specific location
chinchwad.insert(2,"Tejas")
print(chinchwad)

#append adds the new value at the end
chinchwad.append("Nikhil")
print(chinchwad)

#Remove is used to remove a known element
chinchwad.remove("Tejas")
print(chinchwad)

#pop is used to remove the element of the list at a specific position
chinchwad.pop(0)
print(chinchwad)
chinchwad.pop()        # No value specified indicates the value on top of the stack will be deleted
print(chinchwad)

#to add multiple entries in the list
chinchwad.extend(["Ganesh","Rahul","Sandeep","Akshay"])
print(chinchwad)
# pop is used to delete single element where as del is used to delete multiple values
del chinchwad[1:3]
print(chinchwad)

print("**************************************************")
print("Printing minimum of the list")
print(min(chinchwad))

print("**************************************************")
print("Printing the sum")
print(max(chinchwad))

chinchwad[1] = "AAAA"
print(chinchwad)


#id is used to give the address of the variable
print(id(chinchwad))

