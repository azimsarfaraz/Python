mydict = {
    "Pankha":"Fan",
    "Dabba":"Box",
    "Vastu":"Item"
}
print("Options are:", mydict.keys())
a = input("Enter the Hindi word:\n")
print("The meaning of Hindi word is:", mydict.get(a))
