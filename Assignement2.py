#Question no.1

st="Python is a case sensitive language"
length=len(st)
rev=st[::-1]
sl=st[10:26]
idx=st.index("a")
white_spaces=st.strip()
print(st)
print("Length of the string",length)
print(rev)
print(sl)
print(idx)
print(white_spaces)

#Question no.2
name="Maninder Singh"
sid=21102002
dep="Civil"
cg=9.9
det="Hey,{} Here!!\nMy Sid is {}\nI am from {} department and my CGPA is {}".format(name,sid,dep,cg)
print(det)

#Question no.3
a=56
b=10
print(a&b)
print(a|b)
print(a^b)
c=a.__lshift__(2)
d=b.__lshift__(2)
e=a.__rshift__(2)
f=b.__rshift__(4)
print(c)
print(d)
print(e)
print(f)

#Question no.4
st1=input("Enter a string :")
ser="name"
if "name" in st1:
    print("Found!!")
else:
    print("Not Found!!")

#Question no.5
s1=int(input("Enter side of triangle :"))
s2=int(input("Enter side of traingle :"))
s3=int(input("Enter side of triangle :"))
while (s1+s2>s3) and (s1+s3>s2) and (s2+s3>s1):
    print("Triangle is valid")
    break

#Question no.6
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
num = a ^ b
Count_flipped_bit = 0
while (num != 0):
    num = num & (num - 1)
    Count_flipped_bit += 1
print("Number of bits needed to be flipped to convert a to b is:", Count_flipped_bit)