from re import A


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if(a>b and a>c and a>d):
    print("First is the greatest number: " + str(a))
elif(b>a and b>c and b>d):
    print("Second is the greatest number: "+ str(b))
elif(c>a and c>b and c>d):
    print("Third is the greatest number: " + str(c))
else:
    print("Forth is the greatest number: " + str(d))