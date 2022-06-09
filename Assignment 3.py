#1
n1 = int(input("enter the number"))
n2 = bin(n1)
print(n2)
#2
n1= int(input("enter the number"))
operator = input("enter the operator,+,-,*,/")
n2= int(input("enter the second number"))
if operator=="+":
    print(n1+n2)
elif operator=="-":
    print(n1-n2)
elif operator=="*":
    print(n1*n2)
elif operator=="/":
    print(n1/n2)
else:
    print("invalid operator")
#3
import math
#a
print(int(3+4)*5)
#b
n1=int(input("enter the number"))
n2=(n1*(n1-1)/2)
print(n2)
#c
r= int(input("enter the value of r"))
n=4*(math.pi)*(r**2)
print(n)
#d
a= int(input("enter the value of a"))
b=int(input("enter the value of b"))
r=int(input("enter the value of r"))
n=((r*(math.cos(a)**2))+(r*(math.sin(b)**2)))**0.5
print(n)
#e
x1=int(input("enter the value of x1"))
x2=int(input("enter the value of x2"))
y1=int(input("enter the value of y1"))
y2=int(input("enter the value of y2"))
n=float((y2-y1)/(x2-x1))
print(n)
#4
#a
for i in range(5):
    print(i)
#b
for i in range(3,10):
    print(i)
#c
for i in range(4,13,3):
    print(i)
#d
for i in range(15,5,-2):
    print(i)
#e
for i in range(5,3):
    print(i)
#5
h=int(input("enter the value of hydrogen"))
c=int(input("enter the value of carbon"))
o=int(input("enter the value of oxygen"))
n=float(1.00794*h+12.0107*c+15.9994*o)
print(n)