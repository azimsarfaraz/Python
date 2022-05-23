# create a list usin []
a = [23,1,12,6,35]

# print the list using print() function
print(a)

#access using index
print(a[2])

#change the value of list using
a[0]=78
print(a)

#we can create a list of different types
b=[23,'harry',56.56,False]
print(type(b[3]))

#list slicing
c = ['Azim','Saalim','Ali','Monu','Sonu']
print(c[1:4])

print(a+b) #Concatinating lists

a.sort() #sorting in ascending order
print(a)

a.reverse() #reverses the list
print(a)

a.append(37) #adds 37 to the list
print(a)

a.insert(3,8) #inserts 8 at index 3
print(a)

a.pop(3) #removes value from index 3
print(a)

a.remove(37) #removes value 37 from list
print(a)

#check python docs for all list methods

