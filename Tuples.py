#Tuples are not mutable and we cannot change the value
#You have a list and you don't want to change the value then use
#tuple. Since the value of the tuple is not changed , iteration in the
#tuple is very fast
birthday = ('Tejas','12/01/1994', 'Shweta', "12/09/1994")
print(birthday)
print(birthday.count(1))
print(birthday.index('Shweta'))   # Returns the index of a particular value

#type is used to specify the type of the variable
print(type(birthday))