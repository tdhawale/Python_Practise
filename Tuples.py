# Tuples are not mutable and we cannot change the value
# You have a list and you don't want to change the value then use
# tuple. Since the value of the tuple is not changed , iteration in the
# tuple is very fast
location = ("Pimpri", "Chinchwad", "Akurdi", "Khadki")
print("------------------------------------------------------------------")
# Data at location 1
print("The first element is :", location[0])
print("The second element is :", location[1])
print("The third element is :", location[2])
print("The fourth element is :", location[3])
print("------------------------------------------------------------------")
print("Orinting indexed values of the tuple")
# you can also have negative indexes
print("The tuple entries from 3rd element are :", location[2:])
# # # # # # # location[1] = "Lonavala"
# # # # # # # print(location)
# # # # # # # The above statements will give an error becasue we cannot change the tuple values
print("------------------------------------------------------------------")
# You cannot change a tuple since it is unchangable and immutable
# but there is an alternative.
location_temp = list(location)
location_temp[2] = "lonavala"
print("The tuple before changing :", location)
location = location_temp  # this became list so I was able to insert
print("The list after changing :", location)
location.insert(2, "Khandala")
print("The list after inserting new value :", location)
location.remove("Khandala")
print("The list after removing value :", location)
location = tuple(location_temp)
print("The tuple after change", location)
# join two tuples
state = ("Maharashtra", "Karnataka")
city = ("Pune", "bangalore")
india = state + city
print("The join of two tuples is :", india)
