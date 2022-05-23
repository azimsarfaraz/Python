a = {} #empty dictionary
print(type(a)) #type dictionary
b=set() #empty set
print(type(b)) #type set
b.add(4)
b.add(5)
b.add(4) #Adding a value repeatedly does not change a set
# b.add([6,7,8]) #Unable to add list to a set as they are not hashable
b.add((6,7,8)) #Tuples can be added as they are hashable
#b.add({6,7,8}) #Unable to add dictionary to a set as they are not hashable
print(b)

print(len(b)) #Prints the length of this set

b.remove(5) #removes 5 from set
print(b)

print(b.pop()) #removes an element and dislpays as result
b.add(1)
b.add(2)
b.add(3)
print(b)
print(b.union({4,5})) #returns set with all elements
print(b.intersection({3,5}))  #reurns only the same elements