3. Write a Python program to unpack a tuple in several variables. 

l=[]
n=int(input("enter range:"))
print("enter element of list:")
for i in range(0,n):
	y=int(input())
	l.append(y)
t=tuple(l)
print("tuple is:")
print(t)
print("unpacking of tuple is")
a,b,c=t
print(a)
print(b)
print(c)
