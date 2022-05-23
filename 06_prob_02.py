a = int(input("Enter percentage for Subject 1: "))
b = int(input("Enter percentage for Subject 2: "))
c = int(input("Enter percentage for Subject 3: "))

p = (a+b+c)/3
print("Total percentage is: " + str(p))

if(p>40 and a>33 and b>33 and c>33):
    print("Student is passed.")
else:
    print("Student is failed.")