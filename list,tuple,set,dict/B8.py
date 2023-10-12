8. Write a Python program to sort a dictionary by key. 

d={}
n=int(input("Enter range"))
print("enter element of list:")
for i in range(0,n):
	k=input("enter key:")
	v=int(input("enter values:"))
d[k]=v
print("Dictionary is:")
print(d)
x=d.items()
x.sort()
x=dict(d)
print("dictionary sorted by key is:")
print(x)
