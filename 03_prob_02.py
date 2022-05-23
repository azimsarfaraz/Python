a = input("Enter your name: ")
b = input("Enter date:")
c = '''Dear <Name>
You are selected!
Date: <date>'''
c = c.replace("<Name>", a)
c = c.replace("<date>", b)
print(c)
