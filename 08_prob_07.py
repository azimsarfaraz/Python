def rem_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Azim      "
n = rem_and_split(this, "Good")
print(n)