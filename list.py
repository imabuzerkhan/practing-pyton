# i am going to start practicng with list .
# list is mutable in string it can be  changeable 
# list can store multiple value at a time 
# list can  store different datatype value at a time
# Some of the list can return a new list but many of them modify the existing list. (example for reteun new list copy() , sorted())
#sorted() Function
# Does not modify the original list but returns a new sorted list.
# Can be used with any iterable (not just lists), such as tuples, sets, and dictionaries (sorting by keys).
# Returns the sorted version of the iterable without changing the original.

items = ["apple" , "bannana" , "samosa", "pineapple", "pizza"]
print(items) # print item without modify 
print("========================================================")

# i want to change replace banana with babau
items[1] = "babu"
print(items)  # it modify in existing string
print("========================================================")

# using slice method to access the value 
print(items[0:2])
print("========================================================")

# we can also use negative index in list also 
print(items[-1])
print("========================================================")

# using indexing to show the value or change the value it  is possible in list because it is mutable 
print(items[1])
print("========================================================")

# wecan use used append() to add any valuein list 
items.append("abuzer")
print(items)
print("========================================================")
# if what we need abuzer value in the palce of index 1 it is possible or not lets try it 
items.insert(1, "abuzer")
print(items)
print("========================================================")

# using  remove() in list to see how this fun work 
items.remove("abuzer")
print(items) #it only return the first occurrence 
print("========================================================")

# using sort method
value = [22, 400, 34, 1, 67,34,87,21]
value.sort() # it sort the value in accending order
print(value)

# but what we need value in descending order it is to simple do
value = [22, 400, 34, 1, 67,34,87,21]
value.sort(reverse=True)
print(value)

# using reversed method in list 
fruits = ["apple" , "banana" , "kiwi" , "orange" , "grapes"]
fruits.reverse() # its reverse the entire list
fruits.pop() # its remove last from value from the list 
print(fruits.count("banana")) #Count how many times "banana" appears in the list
checkFruite = fruits.index("grapes" , 0 , 5) # its find the index of give data in list 
print(checkFruite)

# using copy method 
copyvalue = fruits.copy() # it return a new list not changed in existing list
print(copyvalue)

#method
number = [1,2,3,4,5,6,7,8,0]
number.clear()  
# #it clear the entire list
print(number)


