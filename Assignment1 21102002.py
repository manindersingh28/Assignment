#Q1 Program to find average of three numbers entered by user

n1=int(input("Enter the number ="))
n2=int(input("Enter the number ="))
n3=int(input("Enter the number ="))
avg=(n1+n2+n3)/3
print("The average of three numbers =",avg)

#Q2 Program to compute a person's income tax

gi=int(input("enter gross income"))
dependent=int(input("number of dependent"))
taxincome=gi-10000-(dependent*3000)
tax=0.2*taxincome  #Tax rate is 20%
print("The person has to pay",tax)

#Q3 Program to store different data types values into a list

n1=int(input("Number of students"))
lts=["Sid","Name","Gender","CourseName","CGPA"]
sid=input("Enter sid")
name=input("Enter name")
gender=input("Enter gender")     #M/F for male and female
cname=input("Enter course name")
cg=input("Enter CPGA")
lst=[sid,name,gender,cname,cg]
print(lts)
print(lst)


#Q4 Program to enter marks of 5 students into a list and display them in sorted manner

m1=float(input("Enter marks of student:"))
m2=float(input("Enter marks of student:"))
m3=float(input("Enter marks of student:"))
m4=float(input("Enter marks of student:"))
m5=float(input("Enter marks of student:"))
mlst=[m1,m2,m3,m4,m5]
mlst.sort()
print(slst)

#Q5
colour=["Red","Green","White","Black","Pink","Yellow"]
colour.pop(3)
print(colour)
colour[3]="Purple"
print(color)