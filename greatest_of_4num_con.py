a = int(input("enter number 1:"))
b = int(input("enter number2:"))
c = int(input("enter number 3:"))
d = int(input("enter number 4:"))

if(a>b and a>c and a>d):
    print("a is greater than all")

elif(b>a and b>c and b>d):
    print("b is greater than all ")

elif(c>a and c>b and c>d):
    print("c is greater than all")
    
elif(d>a and d>b and d>c):
    print("d is greater than all")
