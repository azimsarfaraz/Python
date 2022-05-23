myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "marks": "100",
    "list": [1,2,3],
    "anotherdict": {'harry': 'player'},
    1: 2
}
print(myDict['list'])
#Dictionary methods
print(type(myDict.keys())) #Print the type which is dict_keys for dictionary
print(myDict.keys()) #Print the keys of the dictionary
print(myDict.values()) #Print the values of the dictionary
print(myDict.items()) #Prints the (key.value) for all the contents of dictionary
print(myDict)
updateDict = {
    "Lovish" : "Friend",
    "Harry" : "A Dancer"
}
myDict.update(updateDict) #updates the dictionary by adding key value pairs
print(myDict)

print(myDict.get("harry2")) #If key doesnt exists then it will not throw an error, it will return NULL