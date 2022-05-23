story = '''once upon a time there was a
Cybersecurity expert Azim'''
#String functions
print(len(story)) #length of the string
print(story.endswith("Azim"))   #To check if string is ending with the given word or alphabet, True or False
print(story.count("e"))   #To count a specific alphabet(s) in the string
print(story.capitalize())  #To capatalise first alphabet of the string
print(story.find("upon"))  #To check if given alphabet or word is in the string, output is location if found else -1
print(story.replace("Azim", "Tushar"))  #to replace a word with another one for all occurences
